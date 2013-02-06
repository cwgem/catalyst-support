KERNEL_SUFFIX="3.7.5-hardened"

# Need an initial make.conf file
cat > /etc/make.conf <<MAKECONF
CFLAGS="-O2 -march=athlon64 -pipe"
CXXFLAGS="${CFLAGS}"
CHOST="x86_64-pc-linux-gnu"
MAKEOPTS="-j2"
MAKECONF

# fstab
cat > /etc/fstab <<FSTAB
/dev/xvda1      /               ext4    user_xattr              0 0
FSTAB

# locales
cat > /etc/locale.gen <<LOCALES
en_US ISO-8859-1
en_US.UTF-8 UTF-8
LOCALES
locale-gen

# timezone
cp /usr/share/zoneinfo/UTC /etc/localtime
echo 'UTC' > /etc/timezone

# I'm a vim guy...
echo 'EDITOR="vim"' >> /etc/env.d/99vimeditor

# Ruby 1.9 please
# Also Python 2 support
eselect ruby set ruby19
eselect python set python2.7

# Make eth0 work
cp /etc/init.d/net.lo /etc/init.d/net.eth0
rc-update add net.eth0 default

# Sync the portage tree and eix database
eix-sync -q

# Take care of package moves ahead of time
# by forcing a first run through a package
# pretend. Mainly meant for binary based.
emerge -pv portage

# Give root some basic home directory files
cp -a /etc/skel/.[a-z]* /root/

# and secure it up
chmod -R go-rwsx /root

# This gets the authorized keys from amazon's
# metadata URL at boot
cat > /etc/local.d/ec2.start <<LOCALD
# http://blog.chris-read.net/2007/11/19/ec2-ami-creation-tips/
if [ ! -e /root/.ssh/authorized_keys ]; then
  curl http://169.254.169.254/latest/meta-data/public-keys/0/openssh-key > /tmp/my-key
  if [ \$? -eq 0 ] ; then
    cat /tmp/my-key >> /root/.ssh/authorized_keys
    chmod 600 /root/.ssh/authorized_keys
    rm /tmp/my-key
  fi
fi

hostname \`curl http://169.254.169.254/latest/meta-data/hostname\`
LOCALD
chmod u+x /etc/local.d/ec2.start

# Fix the kernel symlink
rm /usr/src/linux
ln -s "/usr/src/linux-${KERNEL_SUFFIX}" /usr/src/linux

# setup a boot menu
mkdir -p /boot/grub
cat > /boot/grub/menu.lst <<BOOTMENU
default=0
timeout=3
hiddenmenu

title GRsec Kernel
root (hd0)
kernel /boot/kernel-genkernel-x86_64-${KERNEL_SUFFIX} initrd=initramfs-genkernel-x86_64-${KERNEL_SUFFIX} root=/dev/xvda1 ro init=/sbin/init console=hvc0
BOOTMENU

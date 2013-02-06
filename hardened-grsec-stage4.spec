# The subarch can be any of the supported catalyst subarches (like athlon-xp).
# Refer to "man catalyst" or <http://www.gentoo.org/proj/en/releng/catalyst/>
# for supported subarches
# example:
# subarch: athlon-xp
subarch: amd64

# The version stamp is an identifier for the build.  It can be anything you wish# it to be, but it is usually a date.
# example:
# version_stamp: 2006.1
version_stamp: 2013.02.02

# The target specifies what target we want catalyst to do.  For building a CD,
# we start with livecd-stage1 as our target.
# example:
# target: livecd-stage1
target: stage4

# The rel_type defines what kind of build we are doing.  This is merely another
# identifier, but it useful for allowing multiple concurrent builds.  Usually,
# default will suffice.
# example:
# rel_type: default
rel_type: hardened-grsec

# This is the system profile to be used by catalyst to build this target.  It is# specified as a relative path from /usr/portage/profiles.
# example:
# profile: default-linux/x86/2006.1
profile: hardened/linux/amd64

# This specifies which snapshot to use for building this target.
# example:
# snapshot: 2006.1
snapshot: 2013.02.02

# This specifies where the seed stage comes from for this target,  The path is
# relative to $clst_sharedir/builds.  The rel_type is also used as a path prefix# for the seed.
# example:
# default/stage3-x86-2006.1
source_subpath: hardened-grsec/stage3-amd64-2013.02.02

# This is an optional directory containing portage configuration files.  It
# follows the same syntax as /etc/portage and should be consistent across all
# targets to minimize problems.
# example:
# portage_confdir: /etc/portage
portage_confdir: /tools/catalyst/specs/etcportage

# This option specifies the location to a portage overlay that you would like to
# have used when building this target.
# example:
#portage_overlay: /usr/local/portage

# stage4 kernel setup
boot/kernel: hardened
boot/kernel/hardened/sources: =sys-kernel/hardened-sources-3.7.5
boot/kernel/hardened/config: /tools/catalyst/specs/setup/grsec-3.7.5.config
boot/kernel/hardened/packages:
        net-firewall/iptables
        sys-fs/fuse
        sys-fs/lvm2
        sys-fs/squashfs-tools

# services to add
stage4/rcadd: sshd|default vixie-cron|default sysklogd|default lvm|boot ntpd|default

# Quick setup bits
stage4/fsscript: /tools/catalyst/specs/setup/fsscript.sh

# Cleanup some files that catalyst doesn't
stage4/rm: 
	/var/log/emerge-fetch.log
	/var/log/emerge.log
	/var/log/genkernel.log

# The livecd-stage1 target is where you will build packages for your CD.  These
# packages can be built with customized USE settings.  The settings here are
# additive to the default USE configured by the profile.  For building release
# media, the first thing we do is disable all default USE flags with -* and then
# begin to set our own.
# example:
# livecd/use: -* ipv6 socks5 livecd fbcon ncurses readline ssl
stage4/use: ruby

# This is the set of packages that we will merge into the CD's filesystem.  They
# will be built with the USE flags configured above.  These packages must not
# depend on a configured kernel.  If the package requires a configured kernel,
# then it will be defined elsewhere.
# example:
# livecd/packages: livecd-tools dhcpcd acpid apmd gentoo-sources coldplug fxload irssi gpm syslog-ng parted links raidtools dosfstools nfs-utils jfsutils xfsprogs e2fsprogs reiserfsprogs ntfsprogs pwgen rp-pppoe screen mirrorselect penggy iputils hwdata-knoppix hwsetup lvm2 evms vim pptpclient mdadm ethtool wireless-tools prism54-firmware wpa_supplicant
stage4/packages:
        app-admin/sysklogd
        app-crypt/mhash
        app-crypt/shash
        app-editors/vim
        app-misc/tmux
        app-portage/eix
        app-portage/euses
        app-portage/gentoolkit
        app-shells/bash-completion
        app-shells/gentoo-bashcomp
        app-text/asciidoc
        app-text/tree
        app-text/wdiff
        app-vim/eruby-syntax
        app-vim/gentoo-syntax
        app-vim/nginx-syntax
        app-vim/pam-syntax
        app-vim/selinux-syntax
        =dev-lang/ruby-1.8*
	=dev-lang/ruby-1.9*
        dev-ruby/rubygems
        dev-util/patchutils
        dev-util/strace
        dev-vcs/git
        mail-mta/ssmtp
        net-analyzer/netcat
        net-analyzer/tcpdump
        net-analyzer/traceroute
        net-dns/bind-tools
        net-misc/dhcpcd
        net-misc/ntp
        net-misc/stunnel
        net-misc/whois
        sys-apps/ack
	sys-apps/gradm
	sys-apps/mlocate
        sys-apps/paxctl
	=sys-kernel/hardened-sources-3.7.5
        sys-process/at
        sys-process/iotop
        sys-process/lsof
        sys-process/time
        sys-process/vixie-cron
        www-servers/nginx

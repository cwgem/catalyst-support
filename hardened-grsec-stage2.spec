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
target: stage2

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
source_subpath: hardened-grsec/stage1-amd64-2013.02.02

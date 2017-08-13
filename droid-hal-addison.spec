# These and other macros are documented in dhd/droid-hal-device.inc
%define device addison
%define vendor motorola
%define vendor_pretty Motorola
%define device_pretty Moto Z Play
%define installable_zip 1
%define droid_target_armv7hl 1
%define straggler_files \
/init.mmi.boot.sh\
/init.mmi.laser.sh\
%{nil}
%define makefstab_skip_entries /system
%include rpm/dhd/droid-hal-device.inc

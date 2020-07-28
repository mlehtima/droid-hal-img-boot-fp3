%define device fp3

%define mkbootimg_cmd mkbootimg --base 0 --pagesize 2048 --kernel_offset 0x80008000 --ramdisk_offset 0x81000000 --second_offset 0x80f00000 --tags_offset 0x80000100 --cmdline 'androidboot.hardware=qcom msm_rtb.filter=0x237 ehci-hcd.park=3 lpm_levels.sleep_disabled=1 androidboot.bootdevice=7824900.sdhci earlycon=msm_serial_dm,0x78af000 firmware_class.path=/vendor/firmware_mnt/image androidboot.usbconfigfs=true loop.max_part=7 audit=0' --kernel %{kernel} --ramdisk %{initrd} --output

%define root_part_label userdata
%define factory_part_label system_b

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 64

%define lvm_root_size 3000

%include initrd/droid-hal-device-img-boot.inc

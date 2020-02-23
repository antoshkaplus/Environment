## Partitions

### list all installed Linux kernels:
```sudo dpkg --list | egrep -i --color 'linux-image|linux-headers'```

### remove certain kernels:
```sudo apt-get purge linux-image-$version-generic linux-headers-$version-generic linux-headers-$version```

### find all available OS:
```sudo os-prober```

### update EFI bootloader selection
```sudo update-grub```

### moving ubuntu partition
http://www.robotthoughts.com/2018/12/22/moving-the-root-partition-to-a-new-disk-in-ubuntu-18-10-general-grub-chicanery/
instructions won't work unless: go to the new partition and in /etc/fstab update partition UUID using ```sudo blkid```

### swapfile increase:
https://linuxize.com/post/how-to-add-swap-space-on-ubuntu-18-04/

### make hibernate work:
* https://askubuntu.com/questions/6769/hibernate-and-resume-from-a-swap-file
use answer from @gokul, may need dance with ```sudo dpkg-reconfigure -pmedium uswsusp``` 
to get ```sudo s2disk``` working

* make sure "secure boot" turned off in BIOS by @Marc:
https://askubuntu.com/questions/868208/how-to-activate-hibernation-in-16-04-1-systemd

* adding hibernate button to the menu:
http://ubuntuhandbook.org/index.php/2018/05/add-hibernate-option-ubuntu-18-04/

## Monitor & Benchmark

### configure sensors first. hddtemp - for hard disk:
```sudo apt install lm-sensors hddtemp```
```sudo sensors-detect```
```sensors```

### install and run monitor app:
```sudo apt install psensor```

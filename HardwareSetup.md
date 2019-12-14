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

## Monitor & Benchmark

### configure sensors first. hddtemp - for hard disk:
```sudo apt install lm-sensors hddtemp```
```sudo sensors-detect```
```sensors```

### install and run monitor app:
```sudo apt install psensor```

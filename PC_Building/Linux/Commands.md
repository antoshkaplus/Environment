### Kernel command line arguments:
```bash
sudo nano /etc/default/grub
GRUB_CMD_LINUX_DEFAULT="intel_pstate=disable" # disable intel_pstate
GRUB_CMD_LINUX_DEFAULT="cpufreq.default_governor=powersave" # set default governor
sudo update-grub
```
Reboot.  
`intel_pstate` can take values:
* disable
* active
* passive
* force
* no_hwp
* hwp_only
* support_acpi_ppc
* per_cpu_perf_limits


### Scaling governor:
```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor # get
cpupower frequency-set -r -g powersave # set
echo powersave | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor # set 2
```

### Set Governor on reboot
```bash
sudo crontab -e
@reboot cpupower frequency-set -r -g powersave 
```

### Check boot logs: 
```journalctl -b | grep 'something'```

### Check set scaling freq:
```bash
# cpu/cpufreq/policy* and cpu/cpu*/cpufreq are interchangable and point to the same thing.
# made probably for compatibility.
echo 800000 | sudo tee /sys/devices/system/cpu/cpufreq/policy*/scaling_min_freq
echo 4400000 | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq
cat /sys/devices/system/cpu/cpufreq/policy*/scaling_min_freq
```

### Check set `scaling_governor`, `energy_performance_preference` (EPP):
```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_available_governors

sudo cpupower frequency-set -r -g powersave 

cat /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_preference
cat /sys/devices/system/cpu/cpu*/cpufreq/energy_performance_available_preferences
```

### Search settings in kernel configuration file:
```bash
cat /boot/config-"$(uname -r)" | grep GOV
```

### Find file by name:
```bash
find /home/username/ -name "*.err"
```

### Check values of system files group:
```bash
grep . /sys/devices/system/cpu/intel_pstate/*
grep . /sys/devices/system/cpu/cpu0/cpufreq/*
grep . /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```
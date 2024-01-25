`CPU performance scaling` or `CPU frequency scaling` - activity of moving CPU between P-states.

The Linux kernel supports CPU performance scaling by means of the CPUFreq 
(CPU Frequency scaling) subsystem that consists of three layers of code: 
the core, scaling governors and scaling drivers.

CPUFreq allows scaling drivers to bypass the governor layer and 
implement their own performance scaling algorithms. That is done 
by the intel_pstate scaling driver.

### P-states, C-states
*The coprocessor has package-based P-states, core-based C-states 
(which are sometimes referred to as CC-states) and package-based C-states (PC-states). 
It also has the capability to operate in Turbo mode3. There are no per-core based P-states.*

Finally, if the Intel P-State scaling driver is used in active mode, 
the P-State scaling governor will be changed to powersave as it is the only P-State 
scaling governor that allows for the "Energy vs Performance Hints" 
to be taken into consideration, ie. the only P-State scaling governor that allows HWP to work.



If you have `acpi` cpu driver:
$ sudo systemctl disable ondemand.service

Setting CPU governor.
$ echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

Check CPU scaling governor
`cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor` 

Available G:
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors


https://www.thinkwiki.org/wiki/How_to_use_cpufrequtils

https://www.kernel.org/doc/Documentation/cpu-freq/governors.txt#:~:text=The%20%22schedutil%22%20governor%20aims%20at,for%20tasks%20managed%20by%20CFS.

https://stackoverflow.com/questions/72538226/cpufreq-governors-schedutil-missing


https://forum.level1techs.com/t/solved-change-default-cpu-governor/175322/2

Masking Gnome daemon.
https://www.reddit.com/r/archlinux/comments/r41ax3/uninstall_or_disable_gnome_powerprofiledaemon/

https://www.askwoody.com/forums/topic/disabling-a-cpu-feature-intel-turbo-boost/#:~:text=Disabling%20Turbo%20Boost%20completely%20would,is%20actually%20what%20you%20want!
https://github.com/Rongronggg9/power-profiles-daemon/blob/ds/README.md
https://community.intel.com/t5/Software-Tuning-Performance/power-consumption-in-turboboost/td-p/1004179




Now we try to test with disabled intel_pstate:
```bash
sudo nano /etc/default/grub
GRUB_CMD_LINUX_DEFAULT="intel_pstate=disable"
sudo update-grub
```
Reboot.
Check `cpupower freuency-info`

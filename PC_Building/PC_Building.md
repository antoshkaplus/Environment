### Notes:
* managing airflow in the case: 
  https://www.howtogeek.com/303078/
* thermal paste is much better then pads
* before updating BIOS save your current/needed profiles somewhere, 
  as the operation cleans up everything.

### Optimization Tools:

#### Windows:
* Core Temp
* HWMonitor
* Prime95: for stability check AVX2 is not needed. 
    Just make sure usual AVX512 is without errors. It's OK if during AVX testing
    temperatures are about 90. You probably want have it under normal loads.

#### Linux:
* sudo apt install lm-sensors hddtemp    
* sudo apt install psensor  
* psensor - GUI to view system temperatures
* https://linuxhint.com/useful_linux_stress_test_benchmark_cpu_perf/
* Prime95 too.
* s-tui - is really good all-in-one tool to monitor frequencies, temperatures and also stress testing.
    But for stability testing use Prime95.

* to know current cpu frequencies:
```sudo cat /proc/cpuinfo```


### Overclocking CPU:
The best option is to increase Turbo Boost frequency. 
The motherboard has to support overclocking and should provide 
adaptive voltage. Remove limits on power consumption.
It's a good idea to follow what manufacturer did for premium processor 
of the same series.
Be aware that motherboard may not provide individual processor frequency assignment,
even though listed in bios menu (used minimal among all for me).
To support max Turbo Boost per processor assignment, the processor should probably
support Turbo Boost Max 3.0.

From an article: `You hit a wall when your temperatures go over 80C under stress testing, which means you cannot add more voltage unless you increase cooling, so you can't add another multiplier and remain stable.`
Read more: https://www.tweaktown.com/guides/9225/intel-core-i9-9900k-kf-overclocking-guide/index.html

Increasing base frequency undermines all Intel power saving technologies and supposed to wear out the chip quicker. 

Gigabyte guild: https://www.gigabyte.com/FileUpload/Global/multimedia/2/file/525/946.pdf

Ubuntu monitoring:
* https://github.com/torvalds/linux/blob/master/tools/power/x86/turbostat/turbostat.c
* https://software.intel.com/en-us/forums/software-tuning-performance-optimization-platform-monitoring/topic/749357
* wiki.ubuntu.com/OverclockingCpu

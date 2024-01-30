### Notes:
* managing airflow in the case: 
  https://www.howtogeek.com/303078/
* before updating BIOS save your current/needed profiles somewhere, 
  as the operation cleans up everything.


### Thermal Paste Application:
* Thermal paste is much better then pads
* When reapplying thermal paste: remember to tighten cooler 
  screws attached to the motherboard. They get loose during 
  disassembly.
* On rectangular CPUs use 5 dot pattern this time.
  Strive for most coverage and least thickness.


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
* to know current cpu frequencies: `sudo cat /proc/cpuinfo`
* *Monitoring*:
  * Vcore: `watch -n1 'echo "scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192" | bc'`
      from: https://askubuntu.com/questions/876286/how-to-monitor-the-vcore-voltage
      requires: `msr-tools` pkg.
  * Watt: `sudo turbostat -s PkgWatt`
  * Temp/Freq: `s-tui`

*Linux Links*:
* https://www.binarytides.com/monitor-cpu-power-consumption-on-ubuntu/
* https://wiki.ubuntu.com/OverclockingCpu

*Ubuntu monitoring Links*:
* https://github.com/torvalds/linux/blob/master/tools/power/x86/turbostat/turbostat.c
* https://software.intel.com/en-us/forums/software-tuning-performance-optimization-platform-monitoring/topic/749357
* wiki.ubuntu.com/OverclockingCpu

* managing airflow in the case:
https://www.howtogeek.com/303078/

* monitor temperatures:
sudo apt install lm-sensors hddtemp    
sudo apt install psensor  
psensor - GUI to view system temperatures  

* stress test:
https://linuxhint.com/useful_linux_stress_test_benchmark_cpu_perf/

* to know current cpu frequencies:
```sudo cat /proc/cpuinfo```

* thermal paste is much better then pads

### Overclocking CPU:
The best option is to increase Turbo Boost frequency. 
The motherboard has to support overclocking and should provide 
adaptive voltage. Remove limits on power consumption.
It's a good idea to follow what manufacturer did for premium processor 
of the same series.
Be aware that motherboard may not provide individual processor frequency assignment,
even though listed in bios menu (used minimal among all for me).
After overclocking Turbo Boost to 4.9 GHz unable to move further. I believe due to 
power cap as PSU is 450 Watt. And that considering I don't do any work on my video card.

From an article: `You hit a wall when your temperatures go over 80C under stress testing, which means you cannot add more voltage unless you increase cooling, so you can't add another multiplier and remain stable.`
Read more: https://www.tweaktown.com/guides/9225/intel-core-i9-9900k-kf-overclocking-guide/index.html

Increasing base frequency undermines all Intel power saving technologies and supposed to wear out the chip quicker. 


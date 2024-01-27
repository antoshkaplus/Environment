
#### Disable `thermald` (decide for laptop)
```bash
sudo systemctl stop thermald
sudo systemctl disable thermald
```

#### Disable `power-profiles-daemon` (decide for laptop)
```bash
sudo systemctl stop power-profiles-daemon
sudo systemctl mask power-profiles-daemon
```

#### Disable/Remove `cpufreqd` if exists (decide for laptop)
```bash
sudo systemctl stop cpufreqd
sudo systemctl unmask cpufreqd
sudo apt remove cpufreqd
```

#### Check `intel_pstate` driver active
```bash
/sys/devices/system/cpu/intel_pstate/status
```

#### Check `hwp` (HW-managed P-states) enabled, following should be available:
```bash
cat /sys/devices/system/cpu/cpu0/cpufreq/energy_performance_available_preferences
cat /sys/devices/system/cpu/cpu0/cpufreq/energy_performance_preference
```

#### Check `powersave` governor
```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

Check `s-tui` for frequencies and temperature.

#### Overclocking Plan
1. Prime95 | Small FFT | AVX and AVX2 on | Use max cores where no throttle
2. If (1) reduced cores : run all cores with throttle allowed
3. Run s-tui stress test to see real world problem performance.
Each test should run for 10-15 min. 
Final tests should run 30 min.

In our tests we note: 
* max turbo frequency
* Vcore offset
* ambient temp
* idle temp
* max temp seen
* max Vcore seen
* max power consumption seen

On Ubuntu we would need to write a special program to capture 
max values otherwise.
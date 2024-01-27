
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


wiki: <https://gitlab.freedesktop.org/upower/power-profiles-daemon>

power-profiles-daemon offers to modify system behaviour based upon user-selected
power profiles. There are 3 different power profiles, a "balanced" default mode,
a "power-saver" mode, as well as a "performance" mode. The first 2 of those are
available on every system. The "performance" mode is only available on select
systems and is implemented by different "drivers" based on the system or
systems it targets.

In addition to those 2 or 3 modes (depending on the system), "actions" can be hooked
up to change the behaviour of a particular device. For example, this can be used
to disable the fast-charging for some USB devices when in power-saver mode.

GNOME's Settings and shell both include interfaces to select the current mode, but
they are also expected to adjust the behaviour of the desktop depending on the mode,
such as turning the screen off after inaction more aggressively when in power-saver
mode.

Current configuration in:
`/var/lib/power-profiles-daemon/state.ini`

The "driver" for making the hardware act on the user-selected power profile on Intel
CPU-based machines is based on the Intel P-State scaling driver
or the Energy Performance Bias (EPB) feature if available.

It is only used if a platform_profile driver isn't available for the system, and the
CPU supports either hardware-managed P-states (HWP) or Energy Performance Bias (EPB).
Example of a system without platform_profile support but with active P-State
operation mode:
```
$ cat /sys/firmware/acpi/platform_profile_choices
cat: /sys/firmware/acpi/platform_profile_choices: No such file or directory
$ cat /sys/devices/system/cpu/intel_pstate/status
active
```

Example of a system with EPB support:
$ cat /sys/devices/system/cpu/cpu0/power/energy_perf_bias
0

On a laptop I actually have:
cat /sys/devices/system/cpu/cpu0/power/energy_perf_bias
6
It does not change based on profile choice

Finally, if the Intel P-State scaling driver is used in active mode, the P-State
scaling governor will be changed to powersave as it is the only P-State scaling
governor that allows for the "Energy vs Performance Hints" to be taken into consideration,
ie. the only P-State scaling governor that allows HWP to work.

Install the power-profiles-daemon optional dependency (of gnome-control-center) for power profiles support. 
Explicitly starting/enabling the power-profiles-daemon service is unnecessary since 
gnome-shell and GNOME Settings both request its activation upon launching.
When the service is active, power profiles can be managed through the Power section 
of GNOME Settings and in the system menu.


### Activity based on `scaling_governor`.

Somehow when `scaling_governor=performance` you can only have `energy_performance_preference=performance`.
And that means that `power-profiles-daemon` will have no affect. At this point could be easier to just disable it.
But with `scaling_governor=powersave` `energy_performance_available_preferences` can be:
`default performance balance_performance balance_power power`.
Suddenly `power-profiles-daemon` has a meaning, 
it changes `energy_performance_preference` based on power profile:
```
Performance = performance
Balanced = balance_performance
PowerSaver = power
```
If we do the opposite: change `scaling_governor=performance` to `powersave` - `power-profiles-daemon` changes 
`energy_performance_preference` based on the selected profile.

### Control status, besides UI (laptop example):
```
antonsolo@pony:~$ powerprofilesctl set performance
antonsolo@pony:~$ powerprofilesctl 
* performance:
    Driver:     platform_profile
    Degraded:   yes (lap-detected)

  balanced:
    Driver:     platform_profile

  power-saver:
    Driver:     platform_profile
antonsolo@pony:~$ 
```

<https://www.kernel.org/doc/html/v4.19/admin-guide/pm/intel_pstate.html>

Intel P-State driver
--------------------

This driver provides an interface to control the P-State selection for the
SandyBridge+ Intel processors.

P-State doesn't exactly mean a frequency. However, for
the sake of the relationship with cpufreq, P-State and frequency are used
interchangeably.

Understanding the cpufreq core governors and policies are important before
discussing more details about the Intel P-State driver. Based on what callbacks
a cpufreq driver provides to the cpufreq core, it can support two types of
drivers:
* with target_index() callback: In this mode, the drivers using cpufreq core
simply provide the minimum and maximum frequency limits and an additional
interface target_index() to set the current frequency. The cpufreq subsystem
has a number of scaling governors ("performance", "powersave", "ondemand",
etc.). Depending on which governor is in use, cpufreq core will call for
transitions to a specific frequency using target_index() callback. 
* setpolicy() callback: In this mode, drivers do not provide target_index()
callback, so cpufreq core can't request a transition to a specific frequency.
The driver provides minimum and maximum frequency limits and callbacks to set a
policy. The policy in cpufreq sysfs is referred to as the "scaling governor".
The cpufreq core can request the driver to operate in any of the two policies:
"performance" and "powersave". The driver decides which frequency to use based
on the above policy selection considering minimum and maximum frequency limits.

The Intel P-State driver falls under the latter category, which implements the
setpolicy() callback. This driver decides what P-State to use based on the
requested policy from the cpufreq core. If the processor is capable of
selecting its next P-State internally, then the driver will offload this
responsibility to the processor (aka HWP: Hardware P-States). If not, the
driver implements algorithms to select the next P-State.

Since these policies are implemented in the driver, they are not same as the
cpufreq scaling governors implementation, even if they have the same name in
the cpufreq sysfs (scaling_governors). For example the "performance" policy is
similar to cpufreq's "performance" governor, but "powersave" is completely
different than the cpufreq "powersave" governor. The strategy here is similar
to cpufreq "ondemand", where the requested P-State is related to the system load.

Sysfs Interface

In addition to the frequency-controlling interfaces provided by the cpufreq
core, the driver provides its own sysfs files to control the P-State selection.
These files have been added to /sys/devices/system/cpu/intel_pstate/.
Any changes made to these files are applicable to all CPUs (even in a
multi-package system, Refer to later section on placing "Per-CPU limits").

* *max_perf_pct*: Limits the maximum P-State that will be requested by 
      the driver. It states it as a percentage of the available performance. The
      available (P-State) performance may be reduced by the no_turbo
      setting described below.

* *min_perf_pct*: Limits the minimum P-State that will be requested by
      the driver. It states it as a percentage of the max (non-turbo)
      performance level.

* *no_turbo*: Limits the driver to selecting P-State below the turbo
      frequency range.

* *turbo_pct*: Displays the percentage of the total performance that
      is supported by hardware that is in the turbo range. This number
      is independent of whether turbo has been disabled or not.

* *num_pstates*: Displays the number of P-States that are supported
      by hardware. This number is independent of whether turbo has
      been disabled or not.
    
* *hwp_dynamic_boost*: This attribute is only present if intel_pstate works 
      in the active mode with the HWP feature enabled in the processor. If set (equal to 1), 
      it causes the minimum P-state limit to be increased dynamically for a short time 
      whenever a task previously waiting on I/O is selected to run on a given logical CPU 
      (the purpose of this mechanism is to improve performance).
      This setting has no effect on logical CPUs whose minimum P-state limit is directly 
      set to the highest non-turbo P-state or above it.
      
* *energy_efficiency*: P-State is set to offer a "energy_efficiency_enable" node on sysfs that can be enabled to force 
      the more energy efficient CPU mode. Enabling the "Energy Efficiency" mode will help lower power usage 
      and in turn lower heat output and lower power usage, but with the CPU not likely to be running in 
      its highest performance state when needed.

For example, if a system has these parameters:
	Max 1 core turbo ratio: 0x21 (Max 1 core ratio is the maximum P-State)
	Max non turbo ratio: 0x17
	Minimum ratio : 0x08 (Here the ratio is called max efficiency ratio)

Sysfs will show :
	max_perf_pct:100, which corresponds to 1 core ratio
	min_perf_pct:24, max_efficiency_ratio / max 1 Core ratio
	no_turbo:0, turbo is not disabled
	num_pstates:26 = (max 1 Core ratio - Max Efficiency Ratio + 1)
	turbo_pct:39 = (max 1 core ratio - max non turbo ratio) / num_pstates

Refer to "Intel 64 and IA-32 Architectures Software Developer's Manual
Volume 3: System Programming Guide" to understand ratios.

There is one more sysfs attribute in /sys/devices/system/cpu/intel_pstate/status
that can be used for controlling the operation mode of the driver:

      status: Three settings are possible:
      "off"     - The driver is not in use at this time.
      "active"  - The driver works as a P-state governor (default).
      "passive" - The driver works as a regular cpufreq one and collaborates
                  with the generic cpufreq governors (it sets P-states as
                  requested by those governors).
      The current setting is returned by reads from this attribute.  Writing one
      of the above strings to it changes the operation mode as indicated by that
      string, if possible.  If HW-managed P-states (HWP) are enabled, it is not
      possible to change the driver's operation mode and attempts to write to
      this attribute will fail.

cpufreq sysfs for Intel P-State

Since this driver registers with cpufreq, cpufreq sysfs is also presented.
There are some important differences, which need to be considered.

`scaling_cur_freq`: This displays the real frequency which was used during
the last sample period instead of what is requested. Some other cpufreq driver,
like acpi-cpufreq, displays what is requested (Some changes are on the
way to fix this for acpi-cpufreq driver). The same is true for frequencies
displayed at /proc/cpuinfo.

`scaling_governor`: This displays current active policy. Since each CPU has a
cpufreq sysfs, it is possible to set a scaling governor to each CPU. But this
is not possible with Intel P-States, as there is one common policy for all
CPUs. Here, the last requested policy will be applicable to all CPUs. It is
suggested that one use the cpupower utility to change policy to all CPUs at the
same time.

`scaling_setspeed`: This attribute can never be used with Intel P-State.

`scaling_max_freq/scaling_min_freq`: This interface can be used similarly to
the max_perf_pct/min_perf_pct of Intel P-State sysfs. However since frequencies
are converted to nearest possible P-State, this is prone to rounding errors.
This method is not preferred to limit performance.

`affected_cpus`: Not used
`related_cpus`: Not used

For contemporary Intel processors, the frequency is controlled by the
processor itself and the P-State exposed to software is related to
performance levels.  The idea that frequency can be set to a single
frequency is fictional for Intel Core processors. Even if the scaling
driver selects a single P-State, the actual frequency the processor
will run at is selected by the processor itself.

Per-CPU limits

The kernel command line option "intel_pstate=per_cpu_perf_limits" forces
the intel_pstate driver to use per-CPU performance limits.  When it is set,
the sysfs control interface described above is subject to limitations.
- The following controls are not available for both read and write
	/sys/devices/system/cpu/intel_pstate/max_perf_pct
	/sys/devices/system/cpu/intel_pstate/min_perf_pct
- The following controls can be used to set performance limits, as far as the
architecture of the processor permits:
	/sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq
	/sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq
	/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
- User can still observe turbo percent and number of P-States from
	/sys/devices/system/cpu/intel_pstate/turbo_pct
	/sys/devices/system/cpu/intel_pstate/num_pstates
- User can read write system wide turbo status
	/sys/devices/system/cpu/no_turbo

Support of energy performance hints
It is possible to provide hints to the HWP algorithms in the processor
to be more performance centric to more energy centric. When the driver
is using HWP, two additional cpufreq sysfs attributes are presented for
each logical CPU.
These attributes are:
	- energy_performance_available_preferences
	- energy_performance_preference

To get list of supported hints:
$ cat /sys/devices/system/cpu/cpu0/cpufreq/energy_performance_available_preferences
    default performance balance_performance balance_power power

The current preference can be read or changed via cpufreq sysfs
attribute "energy_performance_preference". Reading from this attribute
will display current effective setting. User can write any of the valid
preference string to this attribute. User can always restore to power-on
default by writing "default".

Since threads can migrate to different CPUs, this is possible that the
new CPU may have different energy performance preference than the previous
one. To avoid such issues, either threads can be pinned to specific CPUs
or set the same energy performance preference value to all CPUs.

Tuning Intel P-State driver

When the performance can be tuned using PID (Proportional Integral
Derivative) controller, debugfs files are provided for adjusting performance.
They are presented under:
/sys/kernel/debug/pstate_snb/

The PID tunable parameters are:
      deadband
      d_gain_pct
      i_gain_pct
      p_gain_pct
      sample_rate_ms
      setpoint

To adjust these parameters, some understanding of driver implementation is
necessary. There are some tweeks described here, but be very careful. Adjusting
them requires expert level understanding of power and performance relationship.
These limits are only useful when the "powersave" policy is active.

-To make the system more responsive to load changes, sample_rate_ms can
be adjusted  (current default is 10ms).
-To make the system use higher performance, even if the load is lower, setpoint
can be adjusted to a lower number. This will also lead to faster ramp up time
to reach the maximum P-State.
If there are no derivative and integral coefficients, The next P-State will be
equal to:
	current P-State - ((setpoint - current cpu load) * p_gain_pct)

For example, if the current PID parameters are (Which are defaults for the core
processors like SandyBridge):
      deadband = 0
      d_gain_pct = 0
      i_gain_pct = 0
      p_gain_pct = 20
      sample_rate_ms = 10
      setpoint = 97

If the current P-State = 0x08 and current load = 100, this will result in the
next P-State = 0x08 - ((97 - 100) * 0.2) = 8.6 (rounded to 9). Here the P-State
goes up by only 1. If during next sample interval the current load doesn't
change and still 100, then P-State goes up by one again. This process will
continue as long as the load is more than the setpoint until the maximum P-State
is reached.

For the same load at setpoint = 60, this will result in the next P-State
= 0x08 - ((60 - 100) * 0.2) = 16
So by changing the setpoint from 97 to 60, there is an increase of the
next P-State from 9 to 16. So this will make processor execute at higher
P-State for the same CPU load. If the load continues to be more than the
setpoint during next sample intervals, then P-State will go up again till the
maximum P-State is reached. But the ramp up time to reach the maximum P-State
will be much faster when the setpoint is 60 compared to 97.

Debugging Intel P-State driver

Event tracing
To debug P-State transition, the Linux event tracing interface can be used.
There are two specific events, which can be enabled (Provided the kernel
configs related to event tracing are enabled).

# cd /sys/kernel/debug/tracing/
# echo 1 > events/power/pstate_sample/enable
# echo 1 > events/power/cpu_frequency/enable
# cat trace
gnome-terminal--4510  [001] ..s.  1177.680733: pstate_sample: core_busy=107
	scaled=94 from=26 to=26 mperf=1143818 aperf=1230607 tsc=29838618
		freq=2474476
cat-5235  [002] ..s.  1177.681723: cpu_frequency: state=2900000 cpu_id=2


Using ftrace

If function level tracing is required, the Linux ftrace interface can be used.
For example if we want to check how often a function to set a P-State is
called, we can set ftrace filter to intel_pstate_set_pstate.

# cd /sys/kernel/debug/tracing/
# cat available_filter_functions | grep -i pstate
intel_pstate_set_pstate
intel_pstate_cpu_init
...

# echo intel_pstate_set_pstate > set_ftrace_filter
# echo function > current_tracer
# cat trace | head -15
# tracer: function
#
# entries-in-buffer/entries-written: 80/80   #P:4
#
#                              _-----=> irqs-off
#                             / _----=> need-resched
#                            | / _---=> hardirq/softirq
#                            || / _--=> preempt-depth
#                            ||| /     delay
#           TASK-PID   CPU#  ||||    TIMESTAMP  FUNCTION
#              | |       |   ||||       |         |
            Xorg-3129  [000] ..s.  2537.644844: intel_pstate_set_pstate <-intel_pstate_timer_func
 gnome-terminal--4510  [002] ..s.  2537.649844: intel_pstate_set_pstate <-intel_pstate_timer_func
     gnome-shell-3409  [001] ..s.  2537.650850: intel_pstate_set_pstate <-intel_pstate_timer_func
          <idle>-0     [000] ..s.  2537.654843: intel_pstate_set_pstate <-intel_pstate_timer_func
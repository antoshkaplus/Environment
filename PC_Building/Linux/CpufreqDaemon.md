
Installed with `sudo apt install cpufreqd`.

used to monitor the status of the battery and adjust the frequency of the CPU accordingly 
in order to preserve battery power while providing optimal performance. 
The behaviour of the daemon is fully configurable. Logs are reported through syslogd.

It's configured with file `cat /etc/cpufreqd.conf`, e.g.: 

```editorconfig
[Profile]
name=Performance High
minfreq=100%
maxfreq=100%
policy=performance
#exec_post=echo 8 > /proc/acpi/sony/brightness
[/Profile]
##
# Basic states
##
# when AC use performance mode
[Rule]
name=AC Rule
ac=on                    # (on/off)
profile=Performance High
[/Rule]

##
# Special Rules
##
# CPU Too hot!
[Rule]
name=CPU Too Hot
acpi_temperature=55-100
cpu_interval=50-100
profile=Performance Low
[/Rule]

# use performance mode if I'm watching a movie
# I don't care for batteries! 
# But don't heat too much.
[Rule]
name=Movie Watcher
programs=xine,mplayer,gmplayer
battery_interval=0-100
acpi_temperature=0-60
cpu_interval=0-100
profile=Performance High
[/Rule]
```

The rules are pretty generic. The PC scaling governor becomes unpredictable.
It's probably better to use `thermald` to manage power, 
unless specific features of this service are needed.

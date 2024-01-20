Mobo: GIGABYTE Z790 AORUS Elite AX 
CPU: i7-14700K

Setup optimization is done on Linux.

#### Monitor:
* Vcore: `watch -n1 'echo "scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192" | bc'`
    from: https://askubuntu.com/questions/876286/how-to-monitor-the-vcore-voltage
    requires: `msr-tools` pkg.
* Watt: `sudo turbostat -s PkgWatt`
* Temp/Freq: `s-tui`

#### BIOS disable:
* Hyper-Threading
* Vanderpool Tech (Intel (VMX) Virtualization Tech)
* Turbo Boost Max 3.0
* Intel Dynamic Tuning Technology
* Legacy Game Compatibility Mode

#### Links:
* https://www.binarytides.com/monitor-cpu-power-consumption-on-ubuntu/
* https://wiki.ubuntu.com/OverclockingCpu

The CPU is heating a lot during load. It's hard to cool all cores during Prime95.
CPU is throttling a lot. 

## Stability Testing

### Plan:
1. Prime95 | Small FFT | AVX and AVX2 on
2. Prime95 | Small FFT | AVX on and AVX2 off
3. Prime95 | Small FFT | AVX and AVX2 off
4. Run s-tui stress test to see real world problem performance.
Each test should run for 10-15 min.

In our tests we note: 
* cores frequency range
* max temp seen
* max Vcore seen
* max power consumption seen

On Ubuntu we would need to write a special program to capture 
max values otherwise.

### Progress
#### P@5.5GHz E@4.3GHz. Vcore offset @ 0.
1. Temp Throttle. P:Up to 5.3GHz, E:Up to 4.0GHz. Up to 100C | 1.31V | 280W
2. Temp Throttle. P:Up to 5.5GHz, E:Up to 4.1GHz. Up to 100C | 1.31V | 300W
3. Temp Throttle. P:Up to 5.5GHz, E:Up to 4.2GHz. Up tp 100C | 1.35V | 300W
4. P:5.5, E:4.3 | Up to 81C, but mostly 78C | 1.36V | 230W

#### P@5.5GHz E@4.3GHz. Vcore offset @ -0.05
1. Temp Throttle. P:5.3-5.4, E:3.9-4 | 87-91C | 1.31V | 280W
2. Temp Throttle. P:5.2-5.4, E:4.1-4.2 | 87-90C | 1.33V | 280W
3. Temp Throttle. P:5.4-5.5, E:4-4.2 | 90C | 1.34V | 280W
4. P:5.5, E:4.3 | 72-73C | 1.36V | 215W  
It probably reaches 100 before throttling. 
The setting is on Auto, don't want to change anything.

#### P@5.5GHz E@4.3GHz. Vcore offset @ -0.06
1. Temp Throttle. P:5.2-5.3, E:3.9-4 | 88-91C | 1.31V | 280W  
System restarted in a few minutes. Instability detected.

#### P@5.5GHz E@4.3GHz. Vcore offset @ -0.055
1. Temp Throttle. P:5.3-5.4, E:4 | 91C | 1.34V | 280W  
System restarted in after 9 minutes. Instability detected.

#### P@5.5GHz E@4.3GHz. Vcore offset @ -0.05 | 20 min per test
1. Temp Throttle. P:4.9-5.3, E:3.9-4 | 92C | 1.31V | 280W
System restarted in after 18 minutes. Instability detected.

#### P@5.5GHz E@4.3GHz. Vcore offset @ -0.04 | 30 min per test
1. Temp Throttle. P:4.9-5.5, E:3.9-4 | 100C | 1.34 | 300W
The system looks stable after 36 min but there are overheating problem on some
cores most to least:
CPU: 5,7,3
Cores: 20,28,12
We took the data from turbostat. Core20 has about 10C above others, 
then comes Core28 right after and Core12 has about 5C above others.

At this point we have decided to reapply thermal paste.
Also remember to tighten the base of water cooler on the motherboard after 
taking off watercooler (base bolts get loose). 
We will probably use 5 dot pattern this time.
Strive for most coverage and least thickness.
Mobo: GIGABYTE Z390 Gaming 
CPU: i5-9600K

* Not possible to change default frequency. For some reason CPU working frequency
    stays at Active Turbo Boost frequency.
* Not possible to have per core Active Turbo Boost frequency. 
    Bios will take the lowest value and run all cores with it.

In this case I have decided that the current CPU technologies should not influence 
stability. So, all of them I left Auto/Enabled, except VT-d capability - Disabled,
since I don't plan running virtual machines.

Using available Extreme Memory Profile (X.M.P.).

My goal was to undervolt and maybe move up Turbo Boost frequency a notch. 
Overvolting is not a goal as it generates considerably more heat and consumes plenty of energy. 

Undervolting is achived by offsetting voltage mobo wants to provide the CPU.
This setting is named: `Dynamic Vcore (DVID)`. While `CPU Vcore` should be set to `Normal`.

During monitoring, it's important to remember:
VCore - voltage CPU is using.
VID - voltage CPU is asking for.

### Overclocking / Undervolting:

Intel Performance Optimizer showed frequency 4.8 GHz.

**On Windows**:
* @5 we get > 1.4V on BIOS screen - drop consideration.  
* @4.9 Prime 95 fails AVX2 with blue screen. 
    Without AVX2 still getting an error on one of the workers.
    Could do offsets for AVX but don't consider it worth it.
* @4.8 can do AVX2 temp are in 90s. 
    Got error in the stress test. Without AVX2 the system looks stable.

Cores #2 (init #0) is the hottest, then #3.
To ensure stability we will run Prime95 Small FFT with AVX and AVX2 on.

* Stability was achived @4.7Ghz and -0.045V offset: 1.320V, 168.96W, 91C
* Error discovered on Windows Prime95, reducing to -0.04V offset.

**On Ubuntu**:

Stability test plan:
1. Prime95 | Small FFT | AVX and AVX2 on | Use max cores where no throttle
2. Run s-tui stress test to see real world problem performance.

Results:
* @4.7Ghz | -0.040V offset: 
  1. A:21C | Idle:31C | 90C | 167W | 1.35V
  Error detected.
* @4.7Ghz | -0.035V offset: 
  1. A:21.9C | 91C  | 173W | 1.34V
  Error detected.
* @4.7Ghz | -0.030V offset: 
  1. A:22.2C | Idle:31C | 92C | 176W | 1.34V
  2. A:22.8C | Idle:32C | 68C | 98W | 1.34V  10:04

Done.
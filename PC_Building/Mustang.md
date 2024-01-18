Mobo: Z390 Gaming 
CPU: i5-9600K

Intel performance optimizer showed frequency 4.8 GHz.
@5 we get > 1.4V on BIOS screen - drop consideration.  
@4.9 Prime 95 fails AVX2 with blue screen. 
    Without AVX2 still getting an error on one of the workers.
    Could do offsets for AVX but don't consider it worth it.
@4.8 can do AVX2 temp are in 90s. Processor #2#3 (init #0) get hot.
    Got error in the stress test. Without AVX2 the system looks stable.

* Not possible to change default frequency. For some reason CPU working frequency
    stays at Active Turbo Boost frequency.
* Not possible to have per core Active Turbo Boost frequency. 
    Bios will take the lowest value and run all cores with it.

In this case I have decided that the current CPU technologies should not influence 
stability. So, all of them I left Auto/Enabled, except VT-d capability - Disabled,
since I don't plan running virtual machines.

My goal was to undervolt and maybe move up Turbo Boost frequency a notch. 
Undervolting was achived by offsetting voltage mobo wants to provide the CPU.
This setting is named: `Dynamic Vcore (DVID)`. While `CPU Vcore` should be set to `Normal`.

During monitoring, it's important to remember:
VCore - voltage CPU is using.
VID - voltage CPU is asking for.

To ensure stability we will run Prime95 Small FFT without disabling AVX2.
Monitor CPU Max values: VCore, Power Consumption, Temperature.

Stability was achived at 4.7Ghz and -0.045V offset: 1.320V, 168.96W, 91C

We could try to OC with positive VCore offset, 
but temperature increases and power consumption does not justify it.    
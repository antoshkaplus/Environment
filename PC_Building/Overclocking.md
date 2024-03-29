## Notes:
* Increasing base frequency undermines all Intel power saving technologies 
  and supposed to wear out the chip quicker.
* From an article: `You hit a wall when your temperatures go over 80C under stress testing, which means you cannot add more voltage unless you increase cooling, so you can't add another multiplier and remain stable.`
  Read more: https://www.tweaktown.com/guides/9225/intel-core-i9-9900k-kf-overclocking-guide/index.html
* The best option is to increase Turbo Boost frequency. 
* The motherboard has to support overclocking and should provide 
  adaptive voltage. Remove limits on power consumption.
* It's a good idea to follow what manufacturer did for premium processor 
  of the same series.
* Be aware that motherboard may not provide individual processor frequency assignment,
  even though listed in bios menu (used minimal among all for me).


## Overclocking Stability Test Plan

Each time we should create a stability test plan. 
Here are some components that could be used:
1. Prime95 | Smallest FFT | AVX and AVX2 on (when overhiating with Small FFT) 
2. Prime95 | Small FFT | AVX and AVX2 on

Each test should run for 10-15 min. 
Final tests should run 30 min.

It's also nice to run some real world stress test to see 
measurements, like s-tui stress test.

We should also describe observation measurements: 
* OS (operating system)
* max turbo frequency
* Vcore offset
* ambient temp (A)
* idle temp (Idle)
* max temp seen
* max Vcore seen
* max power consumption seen

On Ubuntu we would need to write a special program to capture 
max values, otherwise user has to do it manually.


In BIOS there is:
* Active Turbo Ratios: Set Turbo based on number of cores in Turbo state.
* Turbo Per Core Limit: Can set maximum Turbo a certain core can reach.
Both of these feautures looks good for tweaking limited number of cores Turbo, 
for specific workloads. In general may not bring that much value. 
All cores Turbo is the main priority.


## Vdroop

Short for voltage droop, it's essentially a situation where voltage can drop way 
too low or also rise way too much. When your system is idling it’s perfectly capable
of holding the voltage you have set in the BIOS. However, under initial heavy load, 
power to your CPU drops and the amount it drops increases as the workload increases. 
Voltage will then rise up quickly. This happens in a blink of an eye, and always 
when your CPU transitions from a state of idle to a state of load. 


## Concepts

CPU: “Hey Mobo, I’m running at 4.9GHz, give me 1.350v. That’s what I normally need.” (VID)
Mobo: “Nah, you’re on a diet. Here’s 1.250v. Deal with it!” (Manual Vcore)
CPU: “But I just started this new workout routine called P95. By the time your 1.250v metabolizes, 
  I can only use 1.150v (Vdroop)”
Mobo: “Fine, here is a preworkout. It will scale up your voltage as load increases to counteract 
  the voltage loss.” (LLC)
CPU: “Awesome dude! Let’s get yoked!”
(A few moments later)
CPU: “Whew. All done with the workout but my heart rate is still high.”
Mobo: “Let me see what I can do. What if I take what you normally need (VID) and offset 
  that by 100mv across the board?” (Offset Vcore)
CPU: “That works for me!”
(A few moments later)
CPU: “Mobo, I have been resting but I feel like I’m going to have a heart attack!”
Mobo: “Dang man, you’re right. Your idle voltage is way too low with that 100mv offset. 
  What about if I just give you 1.250v when you workout and 
  offset 50mv across the board all other times instead?” (Adaptive Vcore)
CPU: “I think that would work best. Thanks bro!”

VCore - voltage CPU is using.
VID - voltage CPU is asking for.


## Overclocking / Undervolting:

The primary goal is to undervolt and maybe move up Turbo Boost frequency a notch. 

If during Prime95 testing, we get throttled by power or temperature,
we should conduct tests on limited numbers of P-cores, E-cores. 
Maybe deactivate P-cores during E-cores testing. It's required to test stability
with a maximum load on a single core.

(1) If in realistic workloads we have available power we can increase Boost frequencies.
If PC becomes unstable - can try to move up a Load-Line Calibration a level. 
It should provide higher voltages during higher loads. With that, monitor
VCore under higher loads - should still be bounds normal for the specific CPU. 

(2) Undervolting is achived by offsetting voltage mobo wants to provide the CPU.
This setting is named: `Dynamic Vcore (DVID)`. While `CPU Vcore` should be set to `Normal`.
We try to increase negative offset and remain stable. 

Here, again, we can apply a trick with Load-Line Calibration to remain 
stable in unrealistic test loads. Make sure it does benefit realistic 
workloads.

### Links:
Gigabyte guild: https://www.gigabyte.com/FileUpload/Global/multimedia/2/file/525/946.pdf

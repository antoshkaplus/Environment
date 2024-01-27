
#### Overclocking Stability Test Plan
1. Prime95 | Small FFT | AVX and AVX2 on | Use max cores where no throttle
2. If (1) reduced cores : run all cores with throttle allowed
3. Run s-tui stress test to see real world problem performance.
Each test should run for 10-15 min. 
Final tests should run 30 min.

In our tests we note: 
* OS (operating system)
* max turbo frequency
* Vcore offset
* ambient temp (A)
* idle temp (Idle)
* max temp seen
* max Vcore seen
* max power consumption seen

On Ubuntu we would need to write a special program to capture 
max values otherwise.

#### Overclocking Stability Test Plan

Each time we should create a stability test plan. 
Here are some components that could be used:
1. Prime95 | Smallest FFT | AVX and AVX2 on (when overhiating with Small FFT) 
2. Prime95 | Small FFT | AVX and AVX2 on

Each test should run for 10-15 min. 
Final tests should run 30 min.

It's also nice to run some real world stress test to see 
measurements, like s-tui stress test.

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
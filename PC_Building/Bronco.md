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
* Vanderpool Tech
* Turbo Boost Max 3.0

#### Links:
* https://www.binarytides.com/monitor-cpu-power-consumption-on-ubuntu/
* https://wiki.ubuntu.com/OverclockingCpu

The CPU is heating a lot during load. It's hard to cool all cores during Prime95.
CPU is throttling a lot. 

## Stability Testing

### Plan:
1. Prime95 | Small FFT | AVX and AVX2 on - with CPU temp throttling.
2. Run (1) but reduce number to eliminate throttling.
3. Prime95 | Small FFT | AVX and AVX2 off - with possible CPU throttling.
4. If (3) is still throttling: reduce number of cores.
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
1. P:5.2-5.3, E:3.9-4.0 sometimes throttles all cores to 3.9 | 
   88C | 1.31V | 280W

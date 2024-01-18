Only Linux is available. So we can monitor:
* Vcore: `watch -n1 'echo "scale=2; $(sudo rdmsr 0x198 -u --bitfield 47:32)/8192" | bc'`
    from: https://askubuntu.com/questions/876286/how-to-monitor-the-vcore-voltage
* Watt Temp: `sudo turbostat -s CoreTmp,PkgTmp,CorWatt,PkgWatt`

Should disable Hyperthreading to improve overall stability.
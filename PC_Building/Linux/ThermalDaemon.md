
Developed by Intel service works alongside `intel_pstate`.
It tries to keep processor cool. 
Uses config in: `cat /etc/thermald/thermal-conf.xml`.

Used alongside other Intel Drivers:
    Intel RAPL power capping driver : Available from Linux kernel 3.13.rc1
    Intel P State driver (Available in Linux kernel stable release)
    Intel Power clamp driver (Available in Linux kernel stable release)
    Intel INT340X drivers
    Intel RAPL-mmio power capping driver: Available from 5.3-rc1

Someone even tried to do a research on it: 
<https://www.phoronix.com/review/intel-thermald-tgl>
Laptop with a processor that does not support `intel_pstate`.

I think it should bring real value on thermally restricted machines.
Laptops are great candidates.

Workstation though, probably don't need this.
Even sample configuration is for a laptop. 

Also on workstations it's pretty hard to get working any fan 
drivers/sensors to work with `thermald`. 

Workstations have different thermal profiles and using thermald would mean
trying to figure out the right configuration.

So far, we just experienced hard throttles when certain temperature reached,
excessive performance cutting.
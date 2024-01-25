Should set up fans in the BIOS. 

Another way is using operating system software. 
Operating systems usually come with a certain `Thermal Management Framework`.  
So if your fans have OS drivers, you could try to manage them better over 
software.

#### On Linux
It's common to not have any fan drivers. The only way - using the BIOS.
But Linux by default comes with `thermald` service that throttles CPU pretty early and does not
let the temperature rise above 70C or something. 
It's possible to disable this service: `sudo systemctl disable thermald`.


#### On Windows
Usually motherboard vendor provides software to download that helps with thermal management control.
While working along with the bios settings it can speed up certain fans during high loads.
For Gigabyte it is EasyTuneEngine.


Fans should be set up based on CPU temp sensor. 
It could be useful to set them up based on other sensors change from ambient temp.  
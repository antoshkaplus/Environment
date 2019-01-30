
**remote debugging:**
gdbserver localhost:12121 /... path to bin file  
gdbserver --attach localhost:12121 pid

**looking for process:** ps auxww|grep <process name>

**grep:**  
egrep 'string1|string2'

**file permisssions:**  
sudo chmod 775 <file name>  
sudo chmod g+rw  
sudo chgrp groupname filename

**tail:**  
sudo tail -f <file name>  
sudo tail -f <file name> | grep program.name   
sudo tail -f -n +1

**copy remote file:**  
scp /path/to/source username@/path/to/destination

**crontab:**
* sudo crontab -l  
* sudo crontab -e

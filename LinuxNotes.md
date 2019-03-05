
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
sudo tail -F \<file name\> *retry if file is not accessible*  
sudo tail -f \<file name\> | grep program.name   
sudo tail -f -n +1

**copy remote file:**  
scp /path/to/source username@/path/to/destination

**crontab:**
* sudo crontab -l  
* sudo crontab -e

**nohup** don't terminate the process if terminal is remote and connection get lost, input and output can be specified but otherwise ignored

**&** execute process in the bg, providing back prompt immediately

**ps aux | grep \<pattern\>** grepping process by name

**top -u \<username\>** tops processes by username

**update env vars from bash** source ~/.bash_profile 


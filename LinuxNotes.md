
**remote debugging:**  
`gdbserver localhost:12121 /... path to bin file`  
`gdbserver --attach localhost:12121 pid`

**looking for process:**  
`ps auxww|grep <process name>`  
``top -p `pgrep python | tr "\\n" "," | sed 's/,$//'` -o %MEM``  
usually used along with `kill -9 PID`

**grep:** `egrep 'string1|string2'`

**look for matching string in all files in path:** `grep -R "string" /path/to/files`

**file permisssions:**  
```
sudo chmod 775 <file name>  
sudo chmod g+rw  
sudo chgrp groupname filename
```

**tail:**  
```
sudo tail -F \<file name\> *retry if file is not accessible*  
sudo tail -f \<file name\> | grep program.name   
sudo tail -f -n +1
```

**copy remote file:**  
scp /path/to/source username@/path/to/destination

**crontab:**
* sudo crontab -l  
* sudo crontab -e

**ssh put process in bg execution**
* want to start in the bg:
`nohup long-running-command &`
* process was already started:
```
ctrl+z
bg
disown -h
```
*nohup* don't terminate the process if terminal is remote and connection get lost, input and output can be specified but otherwise ignored  
*&* execute process in the bg, providing back prompt immediately

**ps aux | grep \<pattern\>** grepping process by name

**top -u \<username\>** tops processes by username

**update env vars from bash** source ~/.bash_profile 

**zip:** zip -r compressed_filename.zip foldername  

**systemd:**  
sudo systemctl daemon-reload  

**update packages**
sudo apt update & sudo apt upgrade

**disc space**: 
df -j
ls -lha

**ssh forwarding:  
`ssh -L 8181:ny4-1.bluefintrading.com:443 anton^logunov@ny4-1.bluefintrading.com`

**journalctl:**
* `journalctl --utc` - view in UTC
* `sudo nano /etc/systemd/journald.conf` - check config
* `journalctl --since= --until=` using `YYYY-MM-DD HH:MM:SS` or “yesterday”, “today”, “tomorrow”, or “now”
You do relative times by prepending “-” or “+” to a numbered value or using words like “ago” in a sentence construction.
`journalctl --since 09:00 --until "1 hour ago"`
* `journalctl -u nginx.service` - filtering by unit
* filter by _PID (process), _GID (group) and _UID (user) id : `journalctl _PID=8088`
* filter by executable path `journalctl path/to/executable`
* `journalctl -p LEVEL` - levels: 0:emerg, 1:alert, 2: crit, 3:err, 4:warning, 5:notice, 6:info, 7:debug
* `journalctl --disk-usage`
* can configure your server to place limits on how much space the journal can take up. This can be done by editing the /etc/systemd/journald.conf file.

**id of the user:**
`id` - get your id
`id -u username` - get someone else's id

**nano control commands:**  
https://monovm.com/post/35/how-to-search-in-nano

Remote debugging

* ssh <host>
* gdbserver localhost:12121 /... path to bin file

* gdbserver --attach localhost:12121 pid

* looking for process:
* ps auxww|grep <process name>

* sudo chmod 775 <file name>


* git clone <host>:<project location>
* cd <project folder name>
* git submodule init 
* git submodule update
* git submodule foreach git checkout master
* git submodule foreach git-pull
* make directories


* $ git push origin --delete <branch_name>

* $ git branch -d <branch_name>

* sudo tail -f <file name>

* sudo tail -f <file name> | grep program.name

* $ git push origin --delete <branch_name>
* $ git branch -d <branch_name>

* copy file:
* scp /path/to/source username@/path/to/destination

* stash to diff:
* git stash show -p stash@{0} > oms.diff
* // make diff from current changes
* git diff >> file.diff

* apply diff:
* git apply change.diff

check if commit was used
git log | grep <commit_id>

* # find first common commit
* git merge-base branch2 branch3

* chmod g+rw
* chgrp groupname filename

* egrep 'string1|string2'


* sudo crontab -l
* sudo crontab -e


* terminal  rm -rf ~/.local/share/Trash/*
* tail -f -n +1

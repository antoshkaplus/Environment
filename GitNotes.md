
**cloning:**  
git clone \<host\>:\<project location\>  
cd \<project folder name\>  
git submodule init  
git submodule update  
git submodule foreach git checkout master  
git submodule foreach git-pull  
make directories  
  
**add submodule:**  
git submodule add -b master [URL to Git repo]  
  
**delete submodule:**
```
git submodule deinit <path_to_submodule>
git rm <path_to_submodule>
git commit-m "Removed submodule "
rm -rf .git/modules/<path_to_submodule>
```

**delete branch:**  
git push origin --delete <branch_name>  
git branch -d <branch_name>  

**delete all local branches**
git branch | xargs git branch -D 

**stash to diff:**  
git stash show -p stash@{0} > oms.diff  
*make diff from current changes*  
git diff >> file.diff  

When working in one branch and need to switch to work on another, can commit current changes.
Later do ```git reset HEAD~ --soft```. If you want to continue working in the same branch, create 
another branch maybe with ```_temp``` suffix. Commit everything there. After your work is done,
do ```git cherry-pick temp_branch --no-commit (-n)``` to get back your changes. Delete temp branch 
afterwards.

**apply diff:**  
git apply change.diff

**check commit used:**  
git log | grep \<commit_id\>  

**find first common commit:**  
git merge-base branch2 branch3  

**remove all local branches except master**  
git branch | grep -v "master" | xargs git branch -D

**when working remotely passphase has to be empty to avoid entering it every time**

**on firewall network git 22 port may be closed, so https should be used and credentials cache**  
git config --global credential.helper 'cache --timeout=3600' (setting is in seconds)

**reset origin**  
git remote set-url origin https://github.com/USERNAME/REPOSITORY.git  

**git config**
```git
[user]
	name = Anton Logunov
	email = antoshkaplus@gmail.com
[core]
	autocrlf = input
[filter "media"]
	required = true
	clean = git media clean %f
	smudge = git media smudge %f
[filter "lfs"]
	clean = git-lfs clean -- %f
	smudge = git-lfs smudge -- %f
	process = git-lfs filter-process
	required = true
[alias]
	st = status
	co = checkout
	dev-merge = !git co master && git pull && git co dev && git merge master && git co master && git merge dev && git push && git co dev
```

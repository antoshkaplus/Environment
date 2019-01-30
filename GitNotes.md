
**cloning:**  
git clone \<host\>:\<project location\>  
cd \<project folder name\>  
git submodule init  
git submodule update  
git submodule foreach git checkout master  
git submodule foreach git-pull  
make directories  
  
**delete branch:**
git push origin --delete <branch_name>
git branch -d <branch_name>

**stash to diff:**  
git stash show -p stash@{0} > oms.diff  
*make diff from current changes*  
git diff >> file.diff  

**apply diff:**  
git apply change.diff

**check commit used:**  
git log | grep \<commit_id\>  

**find first common commit:**  
git merge-base branch2 branch3  

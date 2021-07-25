# Github

## 版本回退

### 查看提交日志

git log

### 查看历史命令

git reflog

可以找到commit id

### 版本回退

git reset --hard HEAD^

### 如何退出日志（log)

q

## 从远程库克隆

 git clone + 地址

其他：

cd +仓库名

ls

查看目录

## 创建与合并分支

git checkout -b <name>

创建分支并切换，相当于

git branch <name>

git checkout <name>



git branch

查看当前分支

 git checkout master 切换回master分支

git merge <name> 合并指定分支到当前分支

**要切换回master分支再进行该条合并命令**

git branch -d <name> 删除dev分支

### switch

git switch -c <name> 创建并切换到已有的分支

git swich master 直接切换到已有的master分支



## 解决冲突

![0](http://tenjoutena.oss-cn-guangzhou.aliyuncs.com/img/0.png)

这种情况下，Git无法执行“快速合并”，只能试图把各自的修改合并起来

一般这种情况下需要手动编辑

## 分支管理

git merge --no-ff -m 'merge with no-ff' <name>

禁用Fast forward，合并并创建一个新的commit

## BUG分支

git stash 把当前工作现场储藏起来

确定要在哪个分支上修复bug，就从哪创建临时分支

git stash list 查看stash列表

git stash apply 恢复不删除

git stash drop 删除

git stash pop 恢复同时把stash删除

在master分支上修复的bug，想要合并到当前dev分支，可以用`git cherry-pick <commit>`命令，把bug提交的修改“复制”到当前分支，避免重复劳动

## Feature分支

如果要丢弃一个没有被合并过的分支，可以通过`git branch -D <name>`强行删除

## 多人协作

如果要推送其他分支 git push origin <name>

1.  首先，可以试图用`git push origin <branch-name>`推送自己的修改；
2.  如果推送失败，则因为远程分支比你的本地更新，需要先用`git pull`试图合并；
3.  如果合并有冲突，则解决冲突，并在本地提交；
4.  没有冲突或者解决掉冲突后，再用`git push origin <branch-name>`推送就能成功！

如果`git pull`提示`no tracking information`，则说明本地分支和远程分支的链接关系没有创建，用命令`git branch --set-upstream-to <branch-name> origin/<branch-name>`。

-   rebase操作可以把本地未push的分叉提交历史整理成直线

-   rebase的目的是使得我们在查看历史提交的变化时更容易，因为分叉的提交需要三方对比。


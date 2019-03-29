####                                                                 Git 基本语法

##### 1.本地库初始化  git init

##### 2.设置签名

作用：区分不同开发人员的身份。

说明：这里设置的签名和登录远程库（代码托管中心）的账户没有关系。

(1)项目级别签名:

**<u>git config user.name [AAA]</u>**

<u>**git config user.email  [邮箱地址]**</u>

签名信息位置：cat .git/config

(2)系统级别签名:

<u>**git config --globaluser.name [AAA]**</u>

<u>**git config --global user.email [邮箱地址]**</u>

签名信息位置：cd ~ 、cat .gitconfig

##### 3.基本操作

(1)查看状态： <u>**git status**</u>(查看工作区、暂存区的状态)

(2)添加操作:  <u>**git add**</u> 文件名(将工作区新建/修改的内容添加到暂存区)

(3)提交操作： **<u>git commit -m “commit message”</u>** 文件名(将暂存区的内容提交到本地库)

##### 4.查看历史记录 

(1**<u>)git log</u>**

(2)<u>**git log --pretty=oneline**</u>

(3)<u>**git log --oneline**</u>

(4)<u>**git reflog (HEAD@{移动到当前版本需要多少步})**</u>

##### 5.前进和后退

(1)基于索引值的操作（推荐做法）

**<u>git reset --hard</u>** 哈希索引值:示例：找回删除状态已经提交本地库的文件操作。

(2)使用^符号 （只能后退，一个^表示后退一步）

<u>**git reset --hard HEAD^**</u>

(3)使用~符号 （只能后退，n表示后退n步）

<u>**git reset --hard HEAD~2**</u>

##### 6.分支常用命令：

(1)<u>**git branch -v**</u> （查看本地库中的所有分支）

(2)<u>**git branch dev**</u> (创建一个新的分支)

(3)<u>**git checkout dev**</u> （切换分支）

(4)分支合并

切换到接收修改的分支

**<u>git checkout master</u>**   (执行merge命令)

**<u>git merge dev</u>**

（注：切换分支后，在dev分支中做出的修改需要合并到被合并的分支master上)
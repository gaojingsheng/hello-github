# 1. 引言
## 1.1. 目的
 统一化管理深度学习和python的开发环境，利用Nvidia Docker的特性，对开发环境实现真正的隔离和便捷地更新迭代。 通过与部署镜像的同步，方便之后深度学习服务的部署。

![](_v_images/20190929110101989_979.png?width=400x)
## 1.2. 镜像介绍
该镜像基于[nvcr.io/nvidia/tensorflow:19.06-py3](https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/rel_19.06.html#rel_19.06https://docs.nvidia.com/deeplearning/frameworks/tensorflow-release-notes/rel_19.06.html#rel_19.06)上的改进实现，加入了常用的开发库和开发工具。本镜像与部署镜像采用相同的Cuda环境，Tensorflow和TensorRT版本。

|工具|版本|
| :-- | :-- |
|CUDA|10.1|
|cuDNN|7.6.0|
|cuBLAS|10.2|
|NCCL|2.4.7|
|Python|3.6|
|G++&GCC|7.4|
|Tensorflow|1.13.1-NV|
|TensorRT|5.1.5|

具体的Python库版本信息可查看[wiki页面](https://wiki.fosun.com/pages/viewpage.action?pageId=33108363)，如有需要增加的库，可以提需求后，编辑[wiki页面](https://wiki.fosun.com/pages/viewpage.action?pageId=33108363)在表格下方增加。
# 2. 镜像使用教程
## 2.1. 镜像下载
+ 镜像名称：alpha-devel: 1.2
+ 镜像下载地址：[harbor](http://harbor.do.proxima-ai.com/harbor/projects/4/repositories)
+ harbor用户名 | 密码：alpha | Alpha987654
+ Dockerfile：[git](http://git.do.proxima-ai.com/cn.aitrox.ai/aidevelopmentlaunch/blob/master/alpha-devel/alpha-devel-1.2/Dockerfile_1.2)
+ Compose file：[git](http://git.do.proxima-ai.com/cn.aitrox.ai/aidevelopmentlaunch/blob/master/alpha-devel/alpha-devel-1.2/docker-compose-env.yml)

## 2.2. Docker compose file 介绍
![](_v_images/20191113142349763_22937.png?width=200x)

+ ports： 由于容器需要做端口映射，对于ssh, jupyter notebook，等需要使用端口的服务需提前分配好端口，避免占用，在这个[wiki页面](https://wiki.fosun.com/pages/viewpage.action?pageId=33114283 
)已经为每个项目团队分配好专属端口。
+ container_name： 每个容器名称只对应一个容器，当开启多个容器时，请注意避免使用同一容器名称。同样，services也请勿使用同一名称。
+ volumes：在做本地目录映射时，请根据每个服务器上具体的硬盘挂载情况，设置相应的映射。

在这个[git页面](http://git.do.proxima-ai.com/cn.aitrox.ai/aidevelopmentlaunch/blob/master/alpha-devel/alpha-devel-1.2/docker-compose-env.yml)已经提供了示例的Docker compose file。
## 2.3. 创建容器
创建指令：
```
sudo docker-compose -f <path_to_your_folder>/docker-compose-env.yml up -d
```
确认创建：

![](_v_images/20190929141655514_3511.png?width=600x)
## 2.4. 容器交互
交互指令：
```
sudo docker exec -it <container_name_or id> <command>
```
交互示例：

![](_v_images/20190929144904034_685.png?width=600x)
# 3. 开发工具使用教程
## 3.1. Jupyter lab & Jupyter notebook
依照这个[wiki页面](https://wiki.fosun.com/pages/viewpage.action?pageId=33114283 
)从每个项目团队专属端口中选择jupyter端口，开启指令：
```
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```
开启示例：

![](_v_images/20190929145641053_20516.png?width=600x)
把生成的URL（上述图中红框）复制到浏览器，把`127.0.0.1`换成`服务器IP`，把端口号`8888`换成`你专属的jupyter端口`。
## 3.2. SSH登陆
依照这个[wiki页面](https://wiki.fosun.com/pages/viewpage.action?pageId=33114283 
)从每个项目团队专属端口中选择ssh端口。
+ IP address: <服务器IP>
+ Username: root
+ Password: 123456
+ Port: `<your_ssh_port>`

提供root账户SSH登陆，登陆指令:
```
ssh root@<server_IP> -p <your_ssh_port>
```
也可以创建自己的用户，创建指令：
```
useradd -d <your_docker_home_directory> -m <user_name>
```
+ `<your_docekr_home_directory>`： 指定用户登入docker 容器时的主目录，建议设置在已映射的本地目录下，如`/hdd/disk2/gupc_docker`，之后若镜像更新，此主目录可以保留。
+ `-m`： 自动建立用户登入的主目录， 不要自动建立请用`-M`。
+ `<user_name>`：所创建的用户名称。

修改用户密码指令：
```
passwd <user_name>
```
给用户赋予sudo权限指令:
```
usermod -aG sudo <user_name>
```
切换到自己创建的用户：
```
su - <user_name>
```
## 3.3. PyCharm
### 3.3.1. X11-forwarding
使用MobaXterm等支持X11-forwarding的SSH客户端登陆容器，若此前在服务器上已安装PyCharm(仅限tar解压安装方式)，使用以下指令即可开PyCharm：
```
cd <path_to_pycharm_folder>/pycharm-*/bin
sh pycharm.sh
```
若此前未曾安装PyCharm, 请使用[PyCharm安装教程](https://www.jetbrains.com/help/pycharm/installation-guide.html)中`Linux`分支`Install using tar archives` 部分教程安装，开启指令同上。
### 3.3.2. SSH远程调试
需要PyCharm Professional版本，[PyCharm官方教程](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html?keymap=primary_default_for_windows)， 未经测试过。
## 3.4. Visual Studio Code:
### 3.4.1. X11-forwarding
使用MobaXterm等支持X11-forwarding的SSH客户端登陆容器，若用root登陆，使用指令：
```
code --user-data-dir <your_user_data_dir>
```
+ `<your_user_data_dir>` ：需要设定一个文件夹存放vscode的用户配置文件。

若用创建用户登陆，使用指令：
```
code
```
### 3.4.2. SSH远程调试
[VSCode官方教程](https://code.visualstudio.com/docs/remote/ssh)，已测试成功。
1. 打开VSCode， 安装 Remote-SSH插件。

![](_v_images/20190929171128632_1836.png?width=200x)

2. `crtl + shift + P`打开`Command Palette`，选择`Remote-SSH：Setting`， 把`Remote.SSH: Allow Local Server Download`勾上。

![](_v_images/20190929171625869_19373.png?width=600x)

3. `crtl + shift + P`打开`Command Palette`，选择`Remote-SSH：Connect to Host...`，选择`Configure SSH Hosts`，选择对应的config。

![](_v_images/20190929172806675_8525.png?width=500x)

4. 在config添加对应的SSH信息。

![](_v_images/20190929173020986_32183.png?width=500x)

5. `crtl + shift + P`打开`Command Palette`，选择`Remote-SSH：Connect to Host...`，选择你刚才增加的SSH Host。

# 4. FAQ
## 4.1 在docker容器内运行某些程序或命令时，报错显示没有权限在该目录下创建文件或文件夹。
为了方便文件传输，docker容器映射了服务器的某些目录至docker容器内，这些映射目录下的某些子目录由于是服务器上用户创建的，所以docker容器内非root用户可能没有写的权限，可以通过以下命令增加权限：
```
sudo chmod 777 -R <your_directory>
```
## 4.2 在docker容器内拷贝了服务器用于文件夹下的某些配置文件夹如`.jupyter`,`.Pycharm`至docker用户目录下却不生效。
这些配置文件夹是服务器上用户创建的，所以需要改变所有者，通过以下命令：
```
sudo chown -R <your_user_name>:<your_user_group> <your_directory>
```
## 4.3 原自动分配gup资源代码`gpu_allocation.py`在docker容器内报错。
在docker 容器内推荐使用新的gpu_allocation.py，代码在[这里](http://git.do.proxima-ai.com/cn.aitrox.ai/aidevelopmentlaunch/blob/master/alpha-devel/UserGuide/gpu_allocation.py)。

## 4.4 在docker容器内无法通过`nvidia-smi`查看gpu进程使用情况。
在Docker compose file内加入`pid: "host”`，可参加[示例Docker compose file](http://git.do.proxima-ai.com/cn.aitrox.ai/aidevelopmentlaunch/blob/master/alpha-devel/alpha-devel-1.2/docker-compose-env.yml)。

## 4.5 docker容器内非root用户无法显示中文。
修改`~/.bashrc`，在末尾加入`export LANG="C.UTF-8" `。然后运行 `source ~/.bashrc`。

## 4.6 docker容器内非root用户无法连外网
修改`~/.bashrc`，在末尾加入`export http_proxy=http://172.16.17.164:3128 export https_proxy=http://172.16.17.164:3128`。然后运行 `source ~/.bashrc`。

# C2C-Web
Software engineering course
环境配置简单参考

## 后端环境配置
Step1:
```bash 
pip install virtualenv 
```
Step2:
```bash
mkdir ~/C2C #或者其他目录，非必须，一个干净的目录即可
cd ~/C2C
virtualenv --no-site-packages -p python3的位置 venv
source ./venv/bin/active 
```
现在进入了一个虚拟的环境，不会受外界干扰也不会干扰外界
Step3:
```bash 
pip install flask
git clone https://github.com/CavsZhouyou/C2C-Web.git
```

## 前端环境配置

Step1: 安装node.js环境，直接官网下载

Step2: 
```bash
在'C2C-Web\webapp\c2c_system'目录下运行命令

npm install
```
注意：可能会报错，报错的情况下再一次运行命令，出现warning没有关系

step3:
```bash
在'C2C-Web\webapp\c2c_system'目录下运行命令

npm run serve
```
运行命令后前端项目跑在9090端口下，访问即可进行开发，已配置热重载

step4:

vue相关文档阅读
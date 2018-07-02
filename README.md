# C2C-Web
Software engineering course
环境配置简单参考

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


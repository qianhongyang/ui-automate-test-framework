UI自动化测试框架 
=====================



## Python版本约束：

仅支持  `Python 3.6+` 
        `Python 3.7+`

## 依赖：
web: 依赖chromdriver，注意浏览器版本相对应，mac把driver放在/usr/local/bin
                                       windows 放在 venv里的scrips                     
Android：第一运行最好通过airtest连接一遍
如果报错：Nonetype error，那么就是adb赋权问题，sudo chmod 777 /你的python环境根目录/site-packages/airtest/core/android/static/adb/mac/adb

ios： 需要xcode，WDA项目，同时开启iproxy
工程招采app--需要提前登录账号，使用ios自动化运行前需要开启的权限：相机、相册、通讯录、定位

### 依赖列表：

版本号仅供参考：

```
Package                 Version  
----------------------- ---------
airtest                 1.1.4    
airtest-selenium        1.0.3    
attrs                   20.2.0   
certifi                 2020.6.20
chardet                 3.0.4    
delayed-assert          0.3.2    
dill                    0.3.2    
hrpc                    1.0.8    
idna                    2.10     
importlib-metadata      1.7.0    
iniconfig               1.0.1    
Jinja2                  2.11.2   
loguru                  0.5.2    
MarkupSafe              1.1.1    
more-itertools          8.5.0    
mss                     4.0.3    
numpy                   1.19.2   
opencv-contrib-python   3.4.2.17 
packaging               20.4     
Pillow                  7.2.0    
pip                     19.0.3   
pluggy                  0.13.1   
pocoui                  1.0.79   
py                      1.9.0    
pynput                  1.7.1    
pyobjc-core             6.2.2    
pyobjc-framework-Cocoa  6.2.2    
pyobjc-framework-Quartz 6.2.2    
pyparsing               2.4.7    
pytest                  5.3.5    
pytest-reportportal     1.0.9    
python-xlib             0.27     
pywinauto               0.6.3    
PyYAML                  5.3.1    
reportportal-client     3.2.3    
requests                2.24.0   
selenium                3.141.0  
setuptools              40.8.0   
six                     1.15.0   
toml                    0.10.1   
urllib3                 1.25.10  
wcwidth                 0.2.5    
websocket-client        0.48.0   
zipp                    3.1.0  
```

### 依赖安装：

执行pip命令安装依赖：

```
pip install -r requirements.txt
```

### pytest执行参数：

请参考`pytest --help`

## 项目文件说明：

```
├── README.md   
├── assets                                          ---------- 资源目录
│   └── font                                         ---------- 字体目录
├── cases                                           ---------- 测试用例目录
│   ├── __init__.py
│   └── ios                                         ---------- ios用例目录
        ├── conftest.py                             ---------- pytest fixtures实现
│       └── iso_app1                                ---------- iso_app1用例目录
│   └── android                                     ---------- 安卓用例目录
        ├── conftest.py                             ---------- pytest fixtures实现
│       └── ad_app1                                ---------- ad_app1用例目录
│   └── web                                         ---------- web用例目录
        ├── conftest.py                                                                                        ---------- pytest fixtures实现
│       ├── __init__.py
│       └── baidu                                     ---------- baidu项目用例目录
│           ├── __init__.py
│           └── test_xxx_xxx.py                     ---------- 用例类文件

├── common                                          ---------- 测试用例公共方法目录
│   ├── __init__.py
│   └── baidu                                         ---------- baidu项目公共方法目录
│       ├── __init__.py
│       └── login.py                                ---------- 例如：通用登录方法

├── config                                          ---------- 配置文件目录
    └── config.yml                                  ---------- 配置文件，内容包含web，ad，ios的配置信息
    
├── log                                             ---------- 日志文件目录
    └── run_log.log                                 ---------- 日志文件
        
    
├── pages                                           ---------- 页面文件目录
│   ├── __init__.py
|   └── app ---------- ios和android统一的页面目录
│       └── ios ---------- ios页面目录
│       └── app-common ---------- app端通用页面目录 如：用poco图片识别可通用的page
│       └── android ---------- android页面目录
│   └── web ---------- web页面目录
│       └── baidu                                     ---------- oms项目页面目录
│           ├── __init__.py
│           └── baidu_main_page.py                       ---------- 例如：登录页面文件，里面写了登录页面的所有元素对象

├── reports                                         ---------- 报告文件目录
    └── pictures                                    ---------- 错误截图文件目录
        └── web_20201001000.png                     ---------- 错误截图文件
    
├── scripts                                         ---------- 脚本文件目录
    └── run.sh                                      ---------- 执行脚本文件
    └── app.sh                                      ---------- app测试执行脚本文件

── utils                                            ---------- 工具文件目录
    ├── android_connect_device.py                   ---------- android连接等
    ├── ...
    └── __init__.py                                 

├── pytest.ini                                      ---------- pytest配置文件
├── requirements.txt                                ---------- 项目依赖
├── runsuite.py                                     ---------- 测试用例执行文件

```
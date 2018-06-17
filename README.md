# 蓝目达数据
蓝目达是一个专门为数字货币开发的行情交易接口，行情接口包含了多个交易所的的行情，分为websocket和restful两种模式，websocket全推模式更为高效。交易接口同样涵盖了多个交易所多个品种。

# 致谢

# 使用对象 
数字货币数据分析师\
数字货币量化交易的个人或团队\
对数字货币交易感兴趣的机构\
分析行情数据的个人或团队\
正在学习pthon及数据分析的人


# 使用前提
安装python3.5以上\
安装pandas5.0以上\
安装ws4py
windows上建议安装Anaconda,是一个集成了python多种库的环境


# 下载安装
方式一：
```bash
pip install eyeblue
```
方式二：\
1.从github上下载\
2.
```bash
python setup.py install
```

# 版本升级
```bash
pip install eyeblue --upgrade
```
查看当前版本

```bash
import eyeblue
print(eyeblue.__versionn__)
```



# API文档

详见help.ipynb

# 交易所，品种参数

详见exchanges_symbols_full.json

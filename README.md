# 蓝目数据
蓝目数据提供了全球各大主流数字资产交易所的全部品种的实时交易行情和各类历史数据，供专业的投资机构和个人宽客使用。数据包含了实时数据ticker, 深度数据depth, 各周期历史kline.并且提供了各个交易所的委托下单、委托撤单、交易信息查询等接口。\
目前支持的数字资产交易所包括：bitfinex, kraken, bitstamp, bittrex, okex, huobi, binance, bitmex,zb, poloniex, bithumb.
提供详细的API访问接口文档，以及针对python, C++ 和java 的客户端访问源码。

[官方网站](https://www.blueye.info)



## 使用对象 
数字货币数据分析师\
数字货币量化交易的个人或团队\
对数字货币交易感兴趣的机构\
分析行情数据的个人或团队\
正在学习pthon及数据分析的人


## 使用前提
安装python3.5以上\
安装pandas5.0以上\
windows上建议安装Anaconda,是一个集成了python多种库的环境
[Anaconda下载](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/)


## 下载安装
方式一：
```bash
pip install eyeblue
```
方式二：\
1.从github上下载
```bash
git clone https://github.com/blueye-info/eyeblue.git
```
2.setup.py安装
```bash
python setup.py install
```

## 版本升级
```bash
pip install eyeblue --upgrade
```
查看当前版本

```bash
import eyeblue
print(eyeblue.__versionn__)
```



## API文档

详见[help.ipynb](https://github.com/blueye-info/eyeblue/blob/master/help.ipynb)\




## 交易所，品种参数

retful行情参数(get相关函数)：\
详见[exchanges_symbols_full.json](https://github.com/blueye-info/eyeblue/blob/master/exchanges_symbols_full.json)
```bash
```

websocket行情参数(wsclient):\
不用交易所行情对应不同ip和port\
详见[client_ip_config.json](https://github.com/blueye-info/eyeblue/blob/master/client_ip_config.json)
[TBotApi.json](https://github.com/blueye-info/eyeblue/blob/master/TBotApi.json)

## 联系客服

QQ: 3405106942  
Email: 3405106942@qq.com

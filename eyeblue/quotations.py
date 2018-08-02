import time
import pandas as pd
from eyeblue import config as cf
from urllib import request


def get_k_data(symbol, k_type, exchange='bitfinex',
               since=0, size=100):

    '''if exchange not in cf.all_exchage:
        raise NameError('exchange not exits')
    else:
        if symbol not in cf.all_ex_sy[exchange]:
            raise NameError('symbol not eixts')
    if k_type not in cf.all_k_type:
        raise NameError('type not eixts')'''

    re_url = 'http://kline.blueye.info/bitquote/v1/kline?' \
             'exchange={}&symbol={}&since={}&size={}&' \
             'type={}'.format(exchange, symbol, since,size, k_type)

    req = request.Request(url=re_url)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')

    data = eval(res)
    t = []
    pd_data = []
    for e in data:
        tmp_data = [e['open'],e['high'],e['low'],
                    e['close'],e['vol']]
        time_local = time.localtime(e['timestamp']/1000)
        date = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        pd_data.append(tmp_data)
        t.append(date)

    k_data = pd.DataFrame(data=pd_data,
                          index=t, dtype=float,
                          columns=['open','high','low',
                                   'close','vol'])
    return k_data


def get_ticker(symbol, exchange='bitfinex'):
    if exchange not in cf.all_exchage:
        raise NameError('exchange not exits')
    else:
        if symbol not in cf.all_ex_sy[exchange]:
            raise NameError('symbol not eixts')

    re_url = 'http://kline.blueye.info/bitquote/v1/ticker?' \
             'exchange={}&symbol={}'.format(exchange,symbol)

    req = request.Request(url=re_url)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')

    data = eval(res)

    return data

def get_depth(symbol, exchange='bitfinex'):
    if exchange not in cf.all_exchage:
        raise NameError('exchange not exits')
    else:
        if symbol not in cf.all_ex_sy[exchange]:
            raise NameError('symbol not eixts')

    re_url = 'http://kline.blueye.info/bitquote/v1/depth?' \
             'exchange={}&symbol={}'.format(exchange,symbol)

    req = request.Request(url=re_url)
    res = request.urlopen(req)
    res = res.read().decode('utf-8')

    data = eval(res)

    return data

import socket
import ssl
from websocket import create_connection
import websocket

while 1:
    ws = create_connection('wss://49.51.228.40:8003/websocket',
                           sslopt={"cert_reqs": ssl.CERT_NONE})
    print(1)
    ws.send('"event":"quote","content":"sub_huobi_$symbol_ticker"')
    print(2)
    print(ws.recv())


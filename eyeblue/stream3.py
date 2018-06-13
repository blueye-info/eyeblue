from ws4py.client.threadedclient import WebSocketClient


class WsClient(WebSocketClient):
    #建立连接时的操作
    def opened(self):
        pass

    #关闭连接时的操作
    def closed(self, code, reason=None):
        pass

    #处理服务器返回的消息
    def received_message(self, m):
        print(m)

if __name__ == '__main__':

    #ws = WsClient('ws://118.25.40.163:8088', protocols=['chat'])
    ws = WsClient('wss://49.51.228.40:8003/websocket',body={"event":"quote","content":"sub_huobi_$symbol_ticker"})
    ws.connect()
    ws.run_forever()
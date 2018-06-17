from ws4py.client.threadedclient import WebSocketClient
import ssl

class WsClient(WebSocketClient):
    def handle_msg(self, m):
        pass

    def opened(self):
        self.send(self.para)

    def closed(self, code, reason=None):
        print('websocket connection closed')


    def received_message(self, m):
        self.handle_msg(m)

def create_ws(url, para, handle_func):
    ws = WsClient(url,protocols=['http-only', 'chat'])
    ws.handle_func = handle_msg
    ws.para = para.encode()

    ws.connect()
    ws.run_forever()

    return ws


if __name__ == '__main__':

    #ws = WsClient('ws://118.25.40.163:8088', protocols=['chat'])

    def handle_msg(m):
        print(123)

    print(1)
    ws = create_ws('wss://49.51.228.40:8003/websocket',
                   '{"event":"quote","content":"sub_huobi_$symbol_ticker"}',
                   handle_msg)

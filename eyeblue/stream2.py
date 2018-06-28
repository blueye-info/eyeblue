import socket
import pprint
import time


class WsClient():
    def __init__(self, ip, port, para, token=' '):
        self.ip = str(ip)
        self.port = int(port)
        self.f = open('log.txt', 'w')

        if token != ' ':
            para = eval(para)
            para['token'] = str(token)
            para = str(para)
        self.para = para.encode()


    def connect(self):
        while True:
            try:
                print('连接中')
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.settimeout(10)

                self.sock.connect((self.ip, self.port))
                print('连接成功')

                self.sock.sendall(self.para)
                return
            except BaseException as e:
                print(e)
                continue


    def run(self):
        self.connect()
        self.sock.settimeout(60)


        while True:
            try:
                msg_len = int(self.sock.recv(4).decode())
                time.sleep(0.07)
                msg = self.sock.recv(msg_len)
                msg = msg.decode()
                #self.handle_msg(msg)
                yield msg
            except BaseException as e:
                print(e)
                self.connect()
                self.f.write('重连\n')
                continue


    def ssl_info(self):
        pprint.pprint(self.ssl_sock.getpeercert())


if __name__ == '__main__':
    ws = WsClient('gw.blueye.info', 5003, '{"event":"quote","content":"sub_huobi_$symbol_ticker"}',
                  token=' ')

    for data in ws.run():
        print(data)
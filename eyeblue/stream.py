import socket
import ssl
import pprint


class WsClient():
    def __init__(self, ip, port, para):
        self.ip = str(ip)
        self.port = int(port)
        self.para = para.encode()
        self.f = open('log.txt', 'w')

    def handle_msg(self, msg):
        pass

    def connect(self):
        while True:
            try:
                print('连接中')
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(10)
                self.ssl_sock = ssl.wrap_socket(sock,
                                                ca_certs="server.crt",
                                                cert_reqs=ssl.CERT_REQUIRED)

                self.ssl_sock.connect((self.ip, self.port))
                print('连接成功')

                self.ssl_sock.sendall(self.para)
                return
            except:
                continue


    def run(self):
        self.connect()

        while True:
            try:
                msg_len = int(self.ssl_sock.recv(4))
                msg = self.ssl_sock.recv(msg_len)
                msg = msg.decode()
                self.handle_msg(msg)
            except:
                self.connect()
                self.f.write('重连\n')
                continue


    def ssl_info(self):
        pprint.pprint(self.ssl_sock.getpeercert())


if __name__ == '__main__':
    def my_handle(m):
        print(m)

    ws = WsClient('gw.blueye.info', 1818, '{"event":"quote","content":"sub_huobi_$symbol_ticker"}')
    ws.handle_msg = my_handle
    ws.run()
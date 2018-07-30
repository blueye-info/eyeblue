import socket
import time
import ssl

class Util():
    def __init__(self):
        self.token = ' '
        self.exchange = 'bittrex'
        self.account_id = '0006'
        
    def get_headlen(self, msg):
        msg_len = len(msg)
        num_zero = 4 - len(str(msg_len))
        zero_list = [0] * num_zero
        re_len = ''
        for e in zero_list:
            re_len += str(e)
        re_len += str(msg_len)
        return re_len

    def login(self, token):
        HOST = '18.144.25.71'
        PORT = 1819

        print('连接中')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        self.con = ssl.wrap_socket(sock,
                                        ca_certs="server.crt",
                                        cert_reqs=ssl.CERT_REQUIRED)
        self.con.connect((HOST, PORT))
        self.token = token

        ts = int(time.time() * 10)
        msg = '45,{},okex,1,btc,next_week,0001,{}'.format(self.token, ts)
        str_len = self.get_headlen(msg)
        msg = str_len + msg

        self.con.sendall(msg.encode())
        length = int(self.con.recv(4).decode())
        re_msg = self.con.recv(length).decode()

        return re_msg

    def order_send(self,symbol_name,price,amount,buy_sell,order_type,
                   open_close, exchange, leverage=0):
        symbol_type = 0
        symbol_info = 0
        ts = int(time.time() * 10)
        msg = '45,{},{},{},{},{},0001,{},{},{},{},{},{},{}'.format\
                (self.token,exchange,symbol_type,symbol_name,symbol_info,
                 ts,price,amount,buy_sell,order_type,open_close,leverage)

        str_len = self.get_headlen(msg)
        msg = str_len + msg

        self.con.sendall(msg.encode())
        length = int(self.con.recv(4).decode())
        re_msg = self.con.recv(length).decode()

        re_list = re_msg.split(',')
        result = int(re_list[-3])
        if result == 1:
            print('order success')
        else:
            print('error code', result[-2])
            print('error msg', re_list[-1])


    def order_kill(self,symbol,order_id,buy_sell=''):
        symbol_type = 0
        symbol_info = 0
        ts = int(time.time() * 10)
        msg = '40,{},{},{},{},{},0001,{},{}'.format(self.token,
               self.exchange, symbol_type, symbol, symbol_info,
               ts, order_id)
        if self.exchange == 'bithumb':
            msg = msg + ',' + str(buy_sell)

        self.con.sendall(msg.encode())
        length = int(self.con.recv(4).decode())
        re_msg = self.con.recv(length).decode()

        re_list = re_msg.split(',')
        result = int(re_list[-3])
        if result == 1:
            print('order success')
            return True
        else:
            print('error code', result[-2])
            print('error msg', re_list[-1])
            return False

    def order_query(self,symbol,order_id):
        symbol_type = 0
        symbol_info = 0
        req_id = 0
        msg = '40,{},{},{},{},{},{},{},{}'.format(self.token,
               self.exchange, symbol_type, symbol, symbol_info,
               self.account_id, req_id, order_id)

        self.con.sendall(msg.encode())
        length = int(self.con.recv(4).decode())
        re_msg = self.con.recv(length).decode()

        return re_msg

    def acount_qurey(self, symbol_type, symbol_info):

        ts = int(time.time() * 10)
        msg = '45,{},okex,1,btc,next_week,0001,{},{},{}'.format(
                self.token, ts, symbol_type, symbol_info)
        str_len = self.get_headlen(msg)
        msg = str_len + msg
        print(msg)


        '''msg = '43,{},{}'.format(symbol_type, symbol_info)
        print(len(msg))
        msg = '0006' + msg
        print(msg)'''

        self.con.sendall(msg.encode())
        length = int(self.con.recv(4).decode())
        re_msg = self.con.recv(length).decode()

        return re_msg



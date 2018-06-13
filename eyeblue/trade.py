import socket

class Util():
    def __init__(self):
        self.token = ' '
        self.exchange = 'bittrex'
        self.account_id = '0006'

    def login(self, name, pwd):
        HOST = '18.144.25.71'
        PORT = 1819
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.con.connect((HOST, PORT))

    def order_send(self,symbol,price,amount,buy_sell,order_type,
                   open_close,leverage=0):
        symbol_type = 0
        symbol_info = 0
        req_id = 0
        msg = '40,{},{},{},{},{},{},{},{},{},{},{},{},{}'.format\
              (self.token,self.exchange,symbol_type,symbol,symbol_info,
               self.account_id,req_id,price,amount,buy_sell,
               order_type,open_close,leverage)

        self.con.sendall(msg.encode())
        len = int(self.con.recv(4).decode())
        re_msg = self.con.recv(len).decode()

        return re_msg

    def order_kill(self,symbol,order_id,buy_sell=''):
        symbol_type = 0
        symbol_info = 0
        req_id = 0
        msg = '40,{},{},{},{},{},{},{},{}'.format(self.token,
               self.exchange, symbol_type, symbol, symbol_info,
               self.account_id, req_id, order_id)
        if self.exchange == 'bithumb':
            msg = msg + ',' + str(buy_sell)

        self.con.sendall(msg.encode())
        len = int(self.con.recv(4).decode())
        re_msg = self.con.recv(len).decode()

        return re_msg

    def order_query(self,symbol,order_id):
        symbol_type = 0
        symbol_info = 0
        req_id = 0
        msg = '40,{},{},{},{},{},{},{},{}'.format(self.token,
               self.exchange, symbol_type, symbol, symbol_info,
               self.account_id, req_id, order_id)

        self.con.sendall(msg.encode())
        len = int(self.con.recv(4).decode())
        re_msg = self.con.recv(len).decode()

        return re_msg

if __name__ == '__main__':
    u = Util()
    u.login(1,1)
    re = u.order_send(symbol='btc_usdt',price=6002,amount=0.01,buy_sell=1,
                 order_type=0,open_close=0)
    #re = u.order_query(symbol='btc_usdt',order_id=-1)
    re = u.order_kill(symbol='btc_usdt',order_id='db4ee279-fe59-4e50-b859-2d34dec5a9ca')
    print(re)
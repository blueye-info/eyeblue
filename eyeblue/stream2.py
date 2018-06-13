import websocket
import websocket
import threading
import time

from gevent import thread


def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(3):
            time.sleep(1)
            data = ws.recv()
            print(data)
        time.sleep(1)

        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())



websocket.enableTrace(True)
ws = websocket.WebSocketApp('wss://49.51.228.40:8003/websocket',
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)

ws.on_open = on_open
import ssl
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE},)
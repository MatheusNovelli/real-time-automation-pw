import socket
import threading
import select
from time import sleep

def synoptic_process():
    print("oio")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8000))
    HEADERSIZE = 10

    while True:
        print("oi")
        str_msg = ""
        new_msg = True

        while True:
            try:
                recv_msg = s.recv(1024)
                print(recv_msg)
            except ValueError as err:
                print(err.args)
            if new_msg:
                msg_size = len(str(recv_msg))
                new_msg = False
            str_msg += recv_msg.decode('utf-8')
            if len(str_msg) == msg_size - 3:
                new_msg = True
                str_msg = ''
            decode_msg = recv_msg.decode('UTF-8').split(',')
            print(decode_msg)
            # print(decode_msg)

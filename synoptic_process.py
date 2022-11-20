import socket, json

def synoptic_process():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostname(), 8000))

    while True:
        str_msg = ""
        new_msg = True

        while True:
            try:
                recv_msg = json.loads(s.recv(1024))
            except ValueError as err:
                # print(err.args)
                pass
            if new_msg:
                msg_size = len(str(recv_msg))
                new_msg = False
            str_msg += recv_msg
            if len(str_msg) == msg_size - 3:
                new_msg = True
                str_msg = ''
            decode_msg = recv_msg.split(',')
            history_file = open("historiador.txt", "a")
            history_file.write(str(decode_msg)+"\n")

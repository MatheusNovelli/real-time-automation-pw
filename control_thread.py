from threading import Thread
import random
import time
from timer import LoopTimer
import global_variables
import socket, json

class ControlThread(Thread):
    def __init__(self, engines_thread, speed_lock, engine_lock, voltage_lock):

        Thread.__init__(self)
        self.speed_lock = speed_lock
        self.engine_lock = engine_lock
        self.voltage_lock = voltage_lock
        self.engines_thread = engines_thread
        self.speed_msg = [0]
        self.running_engines = []

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind((socket.gethostname(), 8000))
        s.listen(5)    

        with self.engine_lock:
            print("Entrou - 1")
            running_engines = []
            max_engines_running = 12
            max_engines = 30

            while len(running_engines) < max_engines_running:
                chosen_engine = random.choice(self.engines_thread)

                #Checando se o motor ou seus motores adjacentes não foram selecionados
                if not any(d["id"] == chosen_engine['id'] for d in running_engines) and not any(d["id"] == chosen_engine['id']+1 for d in running_engines) and not any(d["id"] == chosen_engine['id']-1 for d in running_engines):
                    running_engines.append(chosen_engine)
        
            self.running_engines = running_engines

        for running_engine in running_engines:
            running_engine["value"].start()

        
        time.sleep(1)

        sum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        T = 0.1
        
        with self.speed_lock:
            print("Entrou - 2")

            speed_attr_count = 0
            count = 0
            indexed_speed_ref = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
            
            while True:

                if(running_engines[speed_attr_count]["id"] != count):
                    count += 1

                elif(running_engines[speed_attr_count]["id"] == count):
                    indexed_speed_ref[count] = global_variables.vel_reference[speed_attr_count]
                    speed_attr_count += 1
                    count = 0

                if(speed_attr_count == 12):
                    break

            global_variables.vel_reference = indexed_speed_ref
            print(global_variables.vel_reference)
            
        clientsocket, address = s.accept()
        def control_engine():

            with self.speed_lock:
                with self.voltage_lock:
                    print("Entrou - 3")
                    self.speed_msg = [speed for speed in global_variables.engine_speed]
                    clientsocket.sendall(bytes(json.dumps(str(self.speed_msg)[1:-1]).encode()))
                    # print(global_variables.engine_voltage)
                    # print(global_variables.engine_speed)
                    for i in range(0, max_engines):
                        sum[i] += T*(global_variables.vel_reference[i] - global_variables.engine_speed[i]) 
                        global_variables.engine_voltage[i] = global_variables.vel_reference[i] - global_variables.engine_speed[i] + sum[i]
        timer = LoopTimer(0.2, control_engine)
        timer.start()
        print("Timer startou aqui")
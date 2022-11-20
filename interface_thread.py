from threading import Thread
from time import sleep
import global_variables

class InterfaceThread(Thread):
    def __init__(self, speed_lock, engine_lock):

      Thread.__init__(self)
      self.speed_lock = speed_lock
      self.engine_lock = engine_lock


    def run(self):
        with self.engine_lock:
            with self.speed_lock:
                while(len(global_variables.vel_reference) != 12):
                    vel_input = input("Insira as velocidades para os 12 motores em formato de lista: \nExemplo: [55.2, 40, 87, 45.7, 92.1, 20, 35, 76, 86, 86, 15.2, 42]\n")
                    vel_input_list = vel_input.strip('][').split(', ')
                    global_variables.vel_reference = [float(i) for i in vel_input_list]
                sleep(1)
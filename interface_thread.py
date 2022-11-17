from threading import Thread
from time import sleep
from global_variables import vel_reference

class InterfaceThread(Thread):
    def __init__(self, vel_lock, engine_lock):

      Thread.__init__(self)
      self.vel_lock = vel_lock
      self.engine_lock = engine_lock
      self.vel_reference = vel_reference


    def run(self):
        with self.engine_lock:
            self.vel_lock.acquire()
            print("Entrou na interface")
            while(len(self.vel_reference) != 12):
                vel_input = input("Insira as velocidades para os 12 motores em formato de lista: \nExemplo: [55.2, 40, 87, 45.7, 92.1, 20, 35, 76, 86, 86, 15.2, 42]\n")
                vel_input_list = vel_input.strip('][').split(', ')
                self.vel_reference = [float(i) for i in vel_input_list]
            sleep(1)
            self.vel_lock.release()
            print("Saiu da interface")
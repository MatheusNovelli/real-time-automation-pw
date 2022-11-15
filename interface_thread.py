from threading import Thread

class InterfaceThread(Thread):
    def __init__(self, lock):

      Thread.__init__(self)
      self.lock = lock
      self.vel_reference = None


    def run(self):
        self.lock.acquire()
        print("Entrou na interface")
        self.vel_reference = input("Insira a velocidade dos motores: ")
        self.lock.release()
        print("Saiu da interface")
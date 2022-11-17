from threading import Thread
import random
from time import sleep

class ControlThread(Thread):
    def __init__(self, engines_thread, vel_lock, engine_lock):

        Thread.__init__(self)
        self.vel_lock = vel_lock
        self.engine_lock = engine_lock
        self.engines_thread = engines_thread

    def run(self):
        self.engine_lock.acquire()

        print("Começou a escolha de motores")
        running_engines = []
        max_engines_running = 1

        while len(running_engines) < max_engines_running:
            # chosen_engine = random.choice(self.engines_thread)
            chosen_engine = self.engines_thread[0]


            #Checando se o motor ou seus motores adjacentes não foram selecionados
            if not any(d["id"] == chosen_engine['id'] for d in running_engines) and not any(d["id"] == chosen_engine['id']+1 for d in running_engines) and not any(d["id"] == chosen_engine['id']-1 for d in running_engines):
                running_engines.append(chosen_engine)

        print(running_engines)

        for running_engine in running_engines:
            print(running_engines)
            running_engine["value"].start()
        
        self.engine_lock.release()
        print("Terminou a escolha de motores")

        sleep(1)

        with self.vel_lock:

            print("Controle atribuindo velocidade")
            
            print("Controle parou de atribuir velocidade")

        # with self.voltage_lock:
        #     while True:
        #         for engine in running_engines:





# def main():
#     ControlThread.control_engines()

# if __name__ == "__main__":
#     main()

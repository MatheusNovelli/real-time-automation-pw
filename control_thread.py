from threading import Thread
import random

class ControlThread(Thread):
    def __init__(self, engines_thread, lock):

        Thread.__init__(self)
        self.lock = lock
        self.engines_thread = engines_thread

    def run(self):
        self.lock.acquire()

        print("Começou a escolha de motores")
        running_engines = []
        max_engines_running = 12

        while len(running_engines) < max_engines_running:
            chosen_engine = random.choice(self.engines_thread)

            #Checando se o motor ou seus motores adjacentes não foram selecionados
            if not any(d["id"] == chosen_engine['id'] for d in running_engines) and not any(d["id"] == chosen_engine['id']+1 for d in running_engines) and not any(d["id"] == chosen_engine['id']-1 for d in running_engines):
                running_engines.append(chosen_engine)

        for running_engine in running_engines:
            running_engine["value"].start()
        
        self.lock.release()
        print("Terminou a escolha de motores")


# def main():
#     ControlThread.control_engines()

# if __name__ == "__main__":
#     main()

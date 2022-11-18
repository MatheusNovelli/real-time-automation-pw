from threading import Thread
import random
from time import sleep
import global_variables

class ControlThread(Thread):
    def __init__(self, engines_thread, speed_lock, engine_lock):

        Thread.__init__(self)
        self.speed_lock = speed_lock
        self.engine_lock = engine_lock
        self.engines_thread = engines_thread

    async def run(self):
        self.engine_lock.acquire()

        print("Começou a escolha de motores")
        running_engines = []
        max_engines_running = 12
        max_engines = 30

        while len(running_engines) < max_engines_running:
            chosen_engine = random.choice(self.engines_thread)

            #Checando se o motor ou seus motores adjacentes não foram selecionados
            if not any(d["id"] == chosen_engine['id'] for d in running_engines) and not any(d["id"] == chosen_engine['id']+1 for d in running_engines) and not any(d["id"] == chosen_engine['id']-1 for d in running_engines):
                running_engines.append(chosen_engine)

        print(running_engines)
        
        self.engine_lock.release()
        
        for running_engine in running_engines:
            running_engine["value"].start()
        print("Terminou a escolha de motores")

        
        sleep(1)

        sum = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
        T = 0.1

        with self.speed_lock:
            speed_attr_count = 0
            count = 0
            indexed_speed_ref = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

            print("Controle atribuindo velocidade e fazendo o controle")
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

            i = 0
            while i < 50:
                for i in range(0, max_engines):
                    sum[i] += T*(global_variables.vel_reference[i] - global_variables.engine_speed[i]) 
                    global_variables.engine_voltage[i] = global_variables.vel_reference[i] - global_variables.engine_speed[i] + sum[i]
                i += 1
                # print("Velocidade final dos motores: ",global_variables.engine_speed)

            
                    

            #quando a engine atingir o valor da velocidade de referencia pode dar join()
        print("Controle parou de atribuir velocidade")

        # with self.voltage_lock:
        #     while True:
        #         for engine in running_engines:





# def main():
#     ControlThread.control_engines()

# if __name__ == "__main__":
#     main()

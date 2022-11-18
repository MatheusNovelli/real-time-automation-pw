from threading import Thread, Semaphore
import time
import global_variables

max_increasing_engines = 12
engines_sem = Semaphore(max_increasing_engines)

#Parametros do motor
ra = 0.9 #constante
la = 1 #constante
km = 1
jm = 0.8 #momento de inércia
b = 0.7
kb = 1

# ra = 0.9875 #constante
# la = 0.8355 #constante
# km = 3.16
# jm = 0.1239 #momento de inércia
# b = 0.005219
# kb = 2.45
T = 0.1

class EngineThread(Thread):
    def __init__(self, id, speed_lock):

        Thread.__init__(self)
        self.engine_vel = None
        self.engine_torque = None
        self.id = id
        self.speed_lock = speed_lock

    def run(self):
        print("Motor startou")

        engine_torque = 0 #engine_torque[0] = atual  engine_torque[1] = proxima 
        engine_vel = 0 #engine_vel[0] = atual  engine_vel[1] = proxima 

        # print(engines_sem._value)

        count = 0

        while True:
            # print("XOTA")
            count += 1
            engine_torque = (T*(km * global_variables.engine_voltage[self.id] - km*kb*engine_vel - ra * engine_torque))/la + engine_torque
            # print(engine_torque)
            global_variables.engine_speed[self.id] = (T*(engine_torque - b*global_variables.engine_speed[self.id]))/jm + global_variables.engine_speed[self.id]

            engines_sem.acquire()

            engine_torque = engine_torque
            global_variables.engine_speed[self.id] = global_variables.engine_speed[self.id]
        

            engines_sem.release()
        # algoritmo que aumenta velocidade
        
        time.sleep(1)

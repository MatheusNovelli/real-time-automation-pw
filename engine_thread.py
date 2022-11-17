from threading import Thread, Semaphore
import time

max_increasing_engines = 12
engines_sem = Semaphore(max_increasing_engines)

#Parametros do motor
ra = 0.9 #constante
la = 1 #constante
km = 1
jm = 0.5 #momento de inércia
b = 0.1
kb = 0.013

# ra = 0.9875 #constante
# la = 0.8355 #constante
# km = 3.16
# jm = 0.1239 #momento de inércia
# b = 0.005219
# kb = 2.45
T = 0.1
voltage = 5

class EngineThread(Thread):
    def __init__(self):

        Thread.__init__(self)
        self.engine_vel = None
        self.engine_torque = None

    def run(self):

        engine_torque = 0 #engine_torque[0] = atual  engine_torque[1] = proxima 
        engine_vel = 0 #engine_vel[0] = atual  engine_vel[1] = proxima 

        # print(engines_sem._value)

        count = 0
        list_range = [*range(0, 60)]

        while True:
            count += 1
            engine_torque = (T*(km * voltage - km*kb*engine_vel - ra * engine_torque))/la + engine_torque
            # print(engine_torque)
            engine_vel = (T*(engine_torque - b*engine_vel))/jm + engine_vel
            print("engine_vel", engine_vel)

            engines_sem.acquire()
            engine_torque = engine_torque
            engine_vel = engine_vel
        

            engines_sem.release()
        # algoritmo que aumenta velocidade
        
        time.sleep(1)

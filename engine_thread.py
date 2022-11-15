from threading import Thread, Semaphore
import time

max_increasing_engines = 12
engines_sem = Semaphore(max_increasing_engines)

#Parametros do motor
ra = 1 #constante
la = 0.5 #constante
km = 0.01
jm = 0.1 #momento de inércia
b = 0.1
kb = 0.01
T = 0.1
voltage_motor = 1

class EngineThread(Thread):
    def __init__(self):

        Thread.__init__(self)
        self.engine_vel = None
        self.engine_torque = None

    def run(self):
        engines_sem.acquire()
        engine_torque = 0
        engine_vel = 0

        # print(engines_sem._value)


        while True:
            engine_torque = (T*(km * voltage_motor - km*kb* engine_vel - ra * engine_torque) + engine_torque)/la
            # print(engine_torque)
            engine_vel = (T*(engine_torque - b*engine_vel) + engine_vel)/jm
            # print(engine_vel)

            if engine_vel >= 10:
                break
        
        # print(engine_vel)



        # algoritmo que aumenta velocidade
        engines_sem.release()
        #time.sleep(1)

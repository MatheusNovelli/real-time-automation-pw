from threading import Thread, Semaphore
from timer import LoopTimer
import time
import asyncio
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
        self.engine_torque = 0.0
        self.id = id
        self.speed_lock = speed_lock

    def run(self):
        async def accelerate_engine():
            while True:
                self.engine_torque = (T*(km * global_variables.engine_voltage[self.id] - km*kb* global_variables.engine_speed[self.id] - ra * self.engine_torque))/la + self.engine_torque
                global_variables.engine_speed[self.id] = (T*(self.engine_torque - b*global_variables.engine_speed[self.id]))/jm + global_variables.engine_speed[self.id]
                # engines_sem.acquire()
                # engines_sem.release()
                await asyncio.sleep(0.1)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(accelerate_engine())


        # timer = LoopTimer(0.1, accelerate_engine)
        # timer.start()
        # algoritmo que aumenta velocidade

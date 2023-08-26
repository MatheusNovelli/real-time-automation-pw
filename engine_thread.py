from threading import Thread, Semaphore
import asyncio
import global_variables

max_increasing_engines = 12
engines_sem = Semaphore(max_increasing_engines)

ra = 0.9 
la = 1 
km = 1
jm = 0.8
b = 0.7
kb = 1
T = 0.1

class EngineThread(Thread):
    def __init__(self, id, speed_lock, voltage_lock):

        Thread.__init__(self)
        self.engine_torque = 0.0
        self.id = id
        self.speed_lock = speed_lock
        self.voltage_lock = voltage_lock

    def run(self):
        async def accelerate_engine():
            while True:
                engines_sem.acquire()
                with self.speed_lock:
                    with self.voltage_lock:
                        self.engine_torque = (T*(km * global_variables.engine_voltage[self.id] - km*kb* global_variables.engine_speed[self.id] - ra * self.engine_torque))/la + self.engine_torque
                        global_variables.engine_speed[self.id] = (T*(self.engine_torque - b*global_variables.engine_speed[self.id]))/jm + global_variables.engine_speed[self.id]
                engines_sem.release()
                await asyncio.sleep(0.1)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(accelerate_engine())

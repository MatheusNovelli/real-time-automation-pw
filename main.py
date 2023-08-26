from engine_thread import EngineThread
from control_thread import ControlThread
from interface_thread import InterfaceThread
from threading import Lock
from multiprocessing import Process
from logger_thread import LoggerThread
from synoptic_process import synoptic_process
import global_variables
from timer import LoopTimer
import time

speed_lock = Lock() #Lock para lidar com a velocidade dos motores, que existe em várias threads, como controle, interface e logger
voltage_lock = Lock()
engine_lock = Lock() #Só libera o restante do processo depois que os motores forem escolhidos

def main():
    global_variables.init()
    syn_process = Process(target=synoptic_process)
    max_engine = 30
    engines = [{"value": EngineThread(engine, speed_lock, voltage_lock), "id": engine} for engine in range(0,max_engine)]
    interface_thread = InterfaceThread(speed_lock, engine_lock)
    logger_thread = LoggerThread(speed_lock)
    control_thread = ControlThread(engines, speed_lock, engine_lock, voltage_lock)

    interface_thread.start()
    interface_thread.join()

    logger_thread.start()

    control_thread.start()
    syn_process.start()
    time.sleep(60)
    control_thread.join()
    logger_thread.join()
    syn_process.join()



if __name__ == "__main__":
    main()
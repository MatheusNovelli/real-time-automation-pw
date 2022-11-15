from engine_thread import EngineThread
from control_thread import ControlThread
from interface_thread import InterfaceThread
from threading import Lock, Thread

vel_reference = 0
vel_lock = Lock() #Lock para lidar com a velocidade de referência, que existe em várias threads, como controle, interface e logger
engine_lock = Lock() #Só libera o restante do processo depois que os motores forem escolhidos

def main():
    max_engine = 30
    engines = [{"value": EngineThread(), "id": engine} for engine in range(0,max_engine)]
    interface_thread = InterfaceThread(lock)
    control_thread = ControlThread(engines, engine_lock)
    control_thread.start()
    interface_thread.start()
    interface_thread.join()
    vel_reference = interface_thread.vel_reference
    control_thread.join()

    #ideia de funcionamento
    #control_thread starta
    #interface_thread starta segurando a vel_reference                                                                        
    #interface_thread join
    #control_thread join

if __name__ == "__main__":
    main()
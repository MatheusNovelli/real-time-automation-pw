from engine_thread import EngineThread
from control_thread import ControlThread
from interface_thread import InterfaceThread
from threading import Lock
import global_variables

speed_lock = Lock() #Lock para lidar com a velocidade de referência, que existe em várias threads, como controle, interface e logger
engine_lock = Lock() #Só libera o restante do processo depois que os motores forem escolhidos

def main():
    global_variables.init()

    max_engine = 30
    engines = [{"value": EngineThread(engine, speed_lock), "id": engine} for engine in range(0,max_engine)]
    interface_thread = InterfaceThread(speed_lock, engine_lock)
    interface_thread.start()
    interface_thread.join()
    control_thread = ControlThread(engines, speed_lock, engine_lock)
    control_thread.start()

    # print(vel_reference)

    control_thread.join()
    print("Velocidade de referência", global_variables.vel_reference)

    print("Velocidade final dos motores: ",global_variables.engine_speed)


    #ideia de funcionamento
    #control_thread starta
    #interface_thread starta segurando a vel_reference                                                                        
    #interface_thread join
    #control_thread join

    #ideia metecao de louco
    #control_thread só começa a funcionar depois da interface ter feito tudo, aí foda-se os locks

if __name__ == "__main__":
    main()
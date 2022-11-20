from threading import Thread
from timer import LoopTimer
from time import strftime
import global_variables

class LoggerThread(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):

        def write_log():
            logger_file = open("log.txt", "a")
            logger_file.write(str(global_variables.engine_speed) + " " + strftime('%H:%M:%S') + "\n")

        
        timer = LoopTimer(1, write_log)
        timer.start()
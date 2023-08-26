from threading import Thread
from timer import LoopTimer
from time import strftime
import global_variables

class LoggerThread(Thread):
    def __init__(self, speed_lock):
        Thread.__init__(self)
        self.speed_lock = speed_lock

    def run(self):
        def write_log():
            logger_file = open("log.txt", "a")
            with self.speed_lock:
                logger_file.write(str(global_variables.engine_speed) + " " + strftime('%H:%M:%S') + "\n")

        timer = LoopTimer(1, write_log)
        timer.start()
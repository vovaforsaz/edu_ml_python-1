import random
from random import randint
from log import all_logs
log = all_logs()
class checkses():

    def check_grinding_coffee(self, min=0, max=100):
        self.min = min
        self.max = max
        ran = randint(min, max)
        log.info_log(f"The check_grinding_coffee '{ran}' ", 'check')
        if ran == 0:
            log.info_log(f"The check_grinding_coffee rezult -  {ran} false ", 'check')
            return False
        else:
            log.info_log(f"The check_grinding_coffee rezult - {ran} true ", 'check')
            return True


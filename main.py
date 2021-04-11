from gpiozero import LED
from statechart import Statechart
from yakindu.timer.timer_service import TimerService
import time

class Callback:
    """State machine uses callback operations (here: _synchronize()_).
    """

    led0 = LED(16)
    led1 = LED(26)

    x0 = 0
    x1 = 0

    def __init__(self, statemachine):
        self.sm = statemachine

    def synchronize(self):
        self.x0 = self.sm.counter.x0
        if (self.x0 == 1):
            self.led0.on()
        elif (self.x0 == 0):
            self.led0.off()
            
        self.x1 = self.sm.counter.x1
        if (self.x1 == 1):
            self.led1.on()
        elif (self.x1 == 0):
            self.led1.off()

class Main:

    def __init__(self):
        self.sm = Statechart()
        self.ti = TimerService()
        self.cb = Callback(self.sm)

    def setup(self):
        self.sm.timer_service = self.ti
        self.sm.operation_callback = self.cb
        self.sm.enter()

    def run(self):
        try:
            while True:
                self.sm.user.raise_clock()
                time.sleep(1)
                self.sm.run_cycle()
        except KeyboardInterrupt:
            self.shutdown()

    def shutdown(self):
        print('State machine shuts down.')
        self.sm.exit()
        print('Bye!')

if __name__ == '__main__':
    m = Main()
    m.setup()
    m.run()

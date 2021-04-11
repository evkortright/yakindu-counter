from statechart import Statechart
from yakindu.timer.timer_service import TimerService
import time

class Callback:
    """State machine uses callback operations (here: _synchronize()_).
    """

    x0 = 0
    x1 = 1

    def __init__(self, statemachine):
        self.sm = statemachine

    def synchronize(self):
        self.x0 = self.sm.counter.x0
        self.x1 = self.sm.counter.x1
        print(str(self.x1)+str(self.x0))

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
                print("clock!")
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

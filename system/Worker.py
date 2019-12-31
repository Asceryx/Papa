from threading import Thread, RLock

lock = RLock()


class Worker(Thread):

    def __init__(self, fct, *args):
        Thread.__init__(self)
        self.args = args
        self.fct = fct

    def run(self):
        with lock:
            print(self.args)
            self.fct(*self.args)

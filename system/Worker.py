from threading import Thread, RLock

lock = RLock()


class Worker(Thread):

    def __init__(self, fct, *args):
        Thread.__init__(self)
        self.args = args
        self.fct = [f for f in fct]

    def run(self):
        with lock:
            for f in self.fct:
                f(self.args)

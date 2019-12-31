from threading import Thread, RLock

lock = RLock()


class Worker(Thread):

    def __init__(self, *args):
        Thread.__init__(self)
        self.args = [arg for arg in args]

    def run(self):
        with lock:
            for fct in self.args:
                fct()
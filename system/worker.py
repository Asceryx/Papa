from threading import Thread, RLock


# lock = RLock()


class Worker(Thread):

    def __init__(self, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self._return = None

    def run(self):
        print("[Blinking] : start working threading")
        target = getattr(self, '_target')
        if target is not None:
            self._return = target(*getattr(self, '_args'), **getattr(self, '_kwargs'))

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self._return


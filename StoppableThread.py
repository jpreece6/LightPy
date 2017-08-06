import threading
class StoppableThread(threading.Thread):
    def __init__(self, target=None, name='TestThread', sleepTime=1.0):
        """ constructor, setting initial variables """
        self._stopevent = threading.Event()
        self._sleepperiod = sleepTime
        threading.Thread.__init__(self, name=name, target=target)

    def join(self, timeout=None):
        """ Stop the thread and wait for it to end. """
        self._stopevent.set()
        threading.Thread.join(self, timeout)

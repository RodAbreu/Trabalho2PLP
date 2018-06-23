from threading import Thread, Semaphore, Barrier

class Boat():

    def __init__(self, cap):
        self.cap = cap
        self._mutex = Semaphore(1)
        self._serfqueue = Semaphore(0)      # fila de serfs
        self._hackerqueue = Semaphore(0)    # fila de hackers
        self._barrier = Barrier(4)          # barreira
        self._n_hackers = 0                 # numero de hackers
        self._n_serfs = 0                   # numero de serfs
        self._is_captain = False            

    def signal_barrier(self):
        self._barrier.wait()

    def wait_mutex(self):
        self._mutex.acquire()

    def release_mutex(self):
        self._mutex.release()

    def begin_row(self):
        self._is_captain = True

    def get_total(self):
        return self._n_hackers + self._n_serfs

    def get_n_serfs(self):
        return self._n_serfs

    def get_n_hackers(self):
        return self._n_hackers

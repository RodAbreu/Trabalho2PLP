from threading import Thread, Semaphore, Barrier, Lock

class Boat():

    def __init__(self, cap):
        self.cap = cap
        self._mutex = Lock()                # mutex
        self._serfqueue = Semaphore(4)      # fila de serfs
        self._hackerqueue = Semaphore(4)    # fila de hackers
        self._barrier = Barrier(4)          # barreira
        self._n_hackers = 0                 # numero de hackers
        self._n_serfs = 0                   # numero de serfs
        self._is_captain = False

    def wait_hacker(self):
        self._hackerqueue.acquire()

    def wait_serf(self):
        self._serfqueue.acquire()

    def release_hacker(self):
        self._hackerqueue.release()

    def release_serf(self):
        self._serfqueue.release()

    def signal_barrier(self):
        self._barrier.wait()

    def wait_mutex(self):
        self._mutex.acquire()

    def release_mutex(self):
        self._mutex.release()

    def status_captain(self, estado):
        self._is_captain = estado

    def get_total(self):
        return self._n_hackers + self._n_serfs

    def get_n_serfs(self):
        return self._n_serfs

    def increment_serfs(self):
        self._n_serfs += 1

    def decrement_serfs(self):
        self._n_serfs -= 1

    def get_n_hackers(self):
        return self._n_hackers

    def increment_hackers(self):
        self._n_hackers += 1

    def decrement_hackers(self):
        self._n_hackers -= 1

    def print_boat_fleet(self):
        print('h:',self.get_n_hackers(),', s:',self.get_n_serfs())


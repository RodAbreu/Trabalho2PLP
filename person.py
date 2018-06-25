from abc import ABC, abstractclassmethod
import time

class Person(ABC):

    def __init__(self, p_type):
        self.p_type = p_type    # tipo (hacker ou serf)
        super().__init__()      # chamada do construtor da superclasse

    def row(self, boat):
        
        print('Row!!\n')
        time.sleep(5)

        print("Unload!!\n")
        time.sleep(5)

        boat.status_captain(False)
        boat._n_serfs = 0
        boat._n_hackers = 0

    @abstractclassmethod        
    def board(self, boat):
        pass

class Serf(Person):

    def board(self, boat):
        boat.increment_serfs()
        boat.wait_serf()
        if boat._n_serfs == boat.cap:
            boat.print_boat_fleet()
            boat.signal_barrier()
            boat.status_captain(True)
            boat.wait_mutex()
            self.row(boat)
            boat.release_mutex()
        elif boat._n_hackers == boat.cap/2 and boat._n_serfs == boat.cap/2:
            boat.print_boat_fleet()
            boat.signal_barrier()
            boat.status_captain(True)
            boat.wait_mutex()
            self.row(boat)
            boat.release_mutex()
        else:
            if boat.get_total() >= boat.cap:
                boat.decrement_serfs()
            else:
                boat.print_boat_fleet()
                boat.signal_barrier()

        boat.release_serf()


class Hacker(Person):

    def board(self, boat):
        boat.increment_hackers()
        boat.wait_hacker()
        if boat._n_hackers == boat.cap:
            boat.print_boat_fleet()
            boat.signal_barrier()
            boat.status_captain(True)
            boat.wait_mutex()
            self.row(boat)
            boat.release_mutex()
        elif boat._n_hackers == boat.cap / 2 and boat._n_serfs == boat.cap / 2:
            boat.print_boat_fleet()
            boat.signal_barrier()
            boat.status_captain(True)
            boat.wait_mutex()
            self.row(boat)
            boat.release_mutex()
        else:
            if boat.get_total() >= boat.cap:
                boat.decrement_hackers()
            else:
                boat.print_boat_fleet()
                boat.signal_barrier()

        boat.release_hacker()

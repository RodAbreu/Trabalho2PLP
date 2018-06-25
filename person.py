from abc import ABC, abstractclassmethod
import time

class Person(ABC):

    def __init__(self, p_type):
        self.p_type = p_type    # tipo (hacker ou serf)
        super().__init__()      # chamada do construtor da superclasse

    def row(self, boat):
        # DONE: logica de remada

        print('Row!!\n')
        time.sleep(5)

        print("Unload!!\n")
        boat.release_mutex()

        for x in range(0, boat.cap):
            pass

        boat.status_captain(False)
        pass

    @abstractclassmethod        # metodo abstrato
    def board(self, boat):
        pass

class Serf(Person):

    def board(self, boat):
        # DONE: logica de um novo serf entrando
        boat.increment_serfs()

        #sem_post(&args->boat->serfs_queue);
        boat.release_mutex()

        if boat._n_serfs == boat.cap:
            boat.print_boat_fleet()

            #pthread_barrier_wait(&(args->boat->barrier));    // It signals the barrier
            boat.signal_barrier()

            boat.status_captain(True)

            #pthread_mutex_lock(&args->boat->mutex);
            boat.wait_mutex()

            self.row(boat) #duvida se o is_caption é o do boat
            boat._n_serfs = 0
            pass
        elif boat._n_hackers == boat.cap/2 and boat._n_serfs == boat.cap/2:
            boat.print_boat_fleet()

            #pthread_barrier_wait(&(args->boat->barrier));    // It signals the barrier
            boat.signal_barrier()

            boat.status_captain(True)

            #pthread_mutex_lock(&args->boat->mutex);
            boat.wait_mutex()

            boat._n_hackers = 0
            boat._n_serfs = 0
            pass
        else:
            if boat.get_total() >= boat.cap:
                boat.decrement_serfs()
                pass
            else:
                boat.print_boat_fleet()

                #pthread_barrier_wait(&(args->boat->barrier));
                boat.signal_barrier()

                #pthread_mutex_unlock(&(args->boat->mutex));
                boat.unlock_mutex()
                pass
        pass
        #sem_wait( & args->boat->serfs_queue);
        boat.release_mutex()




class Hacker(Person):

    def board(self, boat):
        # DONE: logica de um novo hacker entrando
        boat.increment_hackers()

        # sem_post(&args->boat->serfs_queue);
        boat.release_mutex()

        if boat._n_hackers == boat.cap:
            boat.print_boat_fleet()

            # pthread_barrier_wait(&(args->boat->barrier));    // It signals the barrier
            boat.signal_barrier()

            boat.status_captain(True)

            # pthread_mutex_lock(&args->boat->mutex);
            boat.wait_mutex()

            self.row(boat)  # duvida se o is_caption é o do boat
            boat._n_hackers = 0
            pass
        elif boat._n_hackers == boat.cap / 2 and boat._n_serfs == boat.cap / 2:
            boat.print_boat_fleet()

            # pthread_barrier_wait(&(args->boat->barrier));    // It signals the barrier
            boat.signal_barrier()

            boat.status_captain(True)

            # pthread_mutex_lock(&args->boat->mutex);
            boat.wait_mutex()

            self.row(boat)
            boat._n_hackers = 0
            boat._n_serfs = 0
            pass
        else:
            if boat.get_total() >= boat.cap:
                boat.decrement_hackers()
                pass
            else:
                boat.print_boat_fleet()

                # pthread_barrier_wait(&(args->boat->barrier));
                boat.signal_barrier()

                # pthread_mutex_unlock(&(args->boat->mutex));
                boat.release_mutex()
                pass
        pass
        # sem_wait( & args->boat->serfs_queue);
        boat.release_mutex()

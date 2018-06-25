from boat import Boat
from threading import Thread
from person import Hacker, Serf
import random

random.seed(None)

boat = Boat(4)
h = Hacker("Hacker")
s = Serf("Serf")


while(True):
    p = Thread(target=h.board, args=(boat,)) if random.choice([True,False]) else Thread(target=s.board, args=(boat,))
    p.start()
    p._delete()
    
p.join()


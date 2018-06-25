from boat import Boat
from threading import Thread
from person import Hacker, Serf
import random

random.seed(None)

boat = Boat(4)
h = Hacker("Hacker")
s = Serf("Serf")


while(True):
    if random.choice([True,False]):
        p = Thread(target=h.board, args=(boat,))  
    else 
        p = Thread(target=s.board, args=(boat,))
    p.start()
    
p.join()


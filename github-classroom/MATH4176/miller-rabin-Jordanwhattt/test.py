import random
from utils import extended_euclidean
from solution import *

boolT = False
a=0

while boolT == False:
    a = random.randrange(2**1023, 2**1024)
    boolT = miller_rabin(a)



print(boolT)




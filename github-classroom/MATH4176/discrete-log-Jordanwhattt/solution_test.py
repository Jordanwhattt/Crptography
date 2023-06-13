from solution import *
def test_dlog():
    p = 4194319 # p is prime
    g = 3       # g is a primitive element mod p
    h = 1234567
    x = dlog(g,h,p,p-1)
    assert pow(g,x,p) == h

def test_indices_of_match():
    L1 = [5,11,2,3,10,19,8,42]
    L2 = [43,12,9,32,19,7,41,59]
    assert indices_of_match(L1,L2) == (5,4)

def test_babysteps_giantsteps():
    p = 4294967311 # p is prime
    g = 3          # g is a primitive element mod p
    h = 1234567891
    x = babysteps_giantsteps(g,h,p,p-1)
    assert pow(g,x,p) == h

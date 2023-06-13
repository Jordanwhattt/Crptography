from utils import extended_euclidean
import random
def factor_2_part(M):
    """Returns k and q such that M=2^k * q, where q is odd."""
    k = 0
    q = 0
    for i in range(0,M):
        if((M // pow(2,i)) % 2 == 1):
            q = (M // pow(2,i))
            k = i
            break
    return k,q

    

    return k, q
    #
def miller_rabin(N, a=None):
    """Returns False if N is composite, and returns
    true if a is not a witness for the compositeness of N
    using the Miller-Rabin test."""
    if a == None:
        a = random.randrange(2,N-1)


    if(N % 2 == 0 ):
        return False

    r,s,t = extended_euclidean(a,N)
    

    if(r > 1 and r < N):
        return False


    k,q = factor_2_part(N-1)
    a = pow(a,q,N)
    if(a-1 % N == 0):
        return True

    for i in range(k):
        if(a % N == N-1):
            return True
        a = pow(a,2,N)
    return False
    #

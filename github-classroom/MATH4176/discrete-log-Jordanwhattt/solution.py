from math import isqrt, floor
def dlog(g,h,p,N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N."""
    if not N: N = p-1
    A = 1
    for x in range(0,p-1):
        if A == pow(h, 1, p):
            return x
        A = pow(A * g, 1, p)
    return None
    #
def indices_of_match(L1, L2):
    """Returns the indices of a common element of the lists L1
    and L2, i.e. a tuple (i,j) such that L1[i] == L2[j]."""
    for i in range(0, len(L1)):
        for j in range(0, len(L2)):
            if(L1[i] == L2[j]):
                return (i, j)
    #
def babysteps_giantsteps(g,h,p,N=None):
    """Returns the discrete logarithm of h with respect to
    the base b modulo p, where g has order N, using Shanks'
    babysteps-giantsteps algorithm."""
    if not N: N = p-1
    M = floor(isqrt(N)) + 1
    baby = {pow(g, i, p) : i for i in range(0, M+1)}
    g_inverse = pow(g, -1, p)
    giant = {pow(h * pow(g_inverse, M*j, p), 1, p):  j for j in range(0 ,M+1)}
    i = None
    j = None
    for key in baby:
        if key in giant:
            i = baby[key]
            j = giant[key]
    if i != None:
            return i+M*j
    return None
    #

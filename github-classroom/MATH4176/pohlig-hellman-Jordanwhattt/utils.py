from math import isqrt
def extended_euclidean(a,b):
    """Returns gcd(a,b) along with integers s,t such that gcd(a,b)=as+bt using
     the extended euclidean algorithm."""

    r_old, r = a,b
    s_old, s = 1,0
    t_old, t = 0,1
    while r > 0:
        q = r_old // r
        r_old, r = r, r_old%r
        s_old, s = s, s_old-s*q
        t_old, t = t, t_old-t*q
    return r_old, s_old, t_old


def modular_inverse(a,m):
    """Returns an integer b such that a*b=1 mod m if gcd(a,m)=1"""
    g,s,t = extended_euclidean(a,m)
    if g != 1:
        raise ValueError('Input must be coprime')
    return s%m

def babysteps_giantsteps(g,h,p,N=None):
    """Returns the discrete log of h with respect to the base g modulo p, where g has order N modulo p.
    """
    if not N: N = p-1
    n = isqrt(N)+1
    # n = floor(sqrt(N))  + 1
    # make a dictionary {g**i%p:i} for fast lookup of the exponent
    babystep = 1
    babysteps_table = {}
    for i in range(n):
        babysteps_table[babystep] = i
        babystep = (babystep * g) % p
    g_inv = modular_inverse(g,p)
    g_n_inv = pow(g_inv, n, p)
    # giantsteps: h*g^(-jn) for j in [0..n-1]
    giantstep = h
    for j in range(n+1):
        if giantstep in babysteps_table:
            i = babysteps_table[giantstep]
            return i+n*j
        giantstep = (giantstep * g_n_inv) % p
    print("no solution!")
    return None

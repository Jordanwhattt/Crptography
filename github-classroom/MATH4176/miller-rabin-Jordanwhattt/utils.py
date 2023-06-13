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

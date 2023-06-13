def extended_euclidean(a,b):

    
    r_prev, r = a, b
    s_prev, s = 1, 0
    t_prev, t = 0, 1
    while r != 0:
        q, r_next = (r_prev // r), (r_prev % r)
        r_prev, r = r, r_next
        s_prev, s = s, s_prev - q*s
        t_prev, t = t, t_prev - q*t

    return r_prev, s_prev, t_prev
    #
def square_and_multiply(g,x,m):

    a, z = g % m, 1
    while x > 0:
        if x % 2 == 1:
            z = (z * a) % m
        a = a**2 % m
        x = x // 2

    return z
    #
def modular_inverse(a,m):
    leng_org = len(bin(m-2))
    b = bin(m-2)[2:leng_org]
    leng = len(b)
    print(b)

    total_r = 1

    for i in range(0, leng):
        r = int(b[leng - i - 1])
        total_r *= (a**(r * 2**i))
        total_r = total_r % m

    return total_r
    #
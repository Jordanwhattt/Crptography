from utils import *
def CRT(moduli, values):
    """Returns an intenger n such that n modulo moduli[i] = values[i].

    Input: moduli - a list of k coprime positive integers
           values - a list of k integers
    """
    c = values[0]
    m = moduli[0]
    k = len(values)
    for i in range(1,k):
        left = pow(values[i] - c, 1, moduli[i])
        right = modular_inverse(m ,moduli[i])
        c += m * pow(left * right, 1, moduli[i])
        m*= moduli[i]

    return pow(c, 1, m)



def q_power_dlog(g,h,p,q,e):
    """Returns the discrete logarithm of g modulo p of h, where g has
    order q^e modulo p."""
    a = pow(g, pow(q, e-1), p)
    b = []
    x = []
    b.append(pow(h, pow(q, e-1, p), p))
    x.append(babysteps_giantsteps(a,b[0], p, q))
    for i in range(1, e):
        exp = 0
        for j in range(0, i):
            exp += x[j] * pow(q, j)
        b.append(pow(h * pow(g, -exp, p), pow(q, e-i-1, p), p))
        x.append(babysteps_giantsteps(a, b[i], p, q))
    temp = 0
    for i in range(0, e):
        temp += x[i] * pow(q, i)
    return temp

def pohlig_hellman(g,h,p,prime_divisors):
    """Returns the discrete logarithm of h with respect to the base g modulo p,
    where p - 1 = q_1^e_1 * ... * q_t^e^_t, and prime_divisors = [[q_1,e_1],...,[q_t,e_t]].
    """
    t = len(prime_divisors)
    N = 1
    for i in range(0,t):
        N*= pow(prime_divisors[i][0], prime_divisors[i][1], p)
    q_arr = []
    e_arr = []
    g_arr = []
    h_arr = []
    y_arr = []

    for i in range(0, t):
        q_i = prime_divisors[i][0]
        e_i = prime_divisors[i][1]

        q_arr.append(q_i)
        e_arr.append(e_i)

        exp_num = N
        exp_dem = pow(q_i, e_i , p)
        exp = pow(exp_num * modular_inverse(exp_dem, p), 1, p)

        g_i = pow(g, exp, p)
        h_i = pow(h, exp, p)
        y_i = q_power_dlog(g_i, h_i, p, q_i, e_i)

        g_arr.append(g_i)
        h_arr.append(h_i)
        y_arr.append(y_i)

    c_arr = []
    for i in range(0 , t):
        c_arr.append(pow(q_arr[i], e_arr[i], p))

    c = CRT(c_arr, y_arr)
    return pow(c, 1, N)



print(CRT([3, 7, 16], [2, 3, 4]))

p = 2 * pow(3, 9) + 1
g = 9
h = pow(9,5)
q = 3
e = 9

print(q_power_dlog(g,h,p,q,e))

p = 211
g = 2
k = 7

h = 2**k
prime_divisors = [[2, 1], [3, 1], [5, 1], [7, 1]]

print(pohlig_hellman(g, h, p, prime_divisors))

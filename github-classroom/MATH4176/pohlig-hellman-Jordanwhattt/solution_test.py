import solution


def test_CRT():
    moduli = [3,7,16]
    values = [2,3,4]
    assert solution.CRT(moduli,values) % 336 == 164

def test_q_power_dlog():
    p = 56843418860808014869689941406251 # p = 2*5^(45) + 1 is prime
    g = 36  # 6 is primitive, 36 has order 5^45 
    q = 5
    e = 45
    x = 12345678910111213141516171819201
    h = pow(g,x,p)
    assert solution.q_power_dlog(g,h,p,q,e) % (5**45) == x

def test_pohlig_hellman():
    prime_divisors = [[2,1],[3,19],[5,19]]
    p = 44336756401062011718751
    g = 3
    x = 12345678910111213141516
    h = pow(g,x,p)
    assert solution.pohlig_hellman(g,h,p,prime_divisors) % (p-1) == x

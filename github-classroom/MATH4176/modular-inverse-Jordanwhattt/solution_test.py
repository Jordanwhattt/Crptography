import solution;

def test_extended_euclidean():
    a = 85520462071
    b = 23529744694
    g,s,t = solution.extended_euclidean(a,b)
    assert g == a*s + b*t
def test_square_and_multiply():
    a = 1234567
    x = 7891011
    m = 7654321
    assert solution.square_and_multiply(a,x,m) == pow(a,x,m)
def test_modular_inverse():
    a = 141
    m = 541
    b = solution.modular_inverse(a,m)
    assert (a*b)%m == 1

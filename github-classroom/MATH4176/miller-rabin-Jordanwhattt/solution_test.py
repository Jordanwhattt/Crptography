from solution import factor_2_part, miller_rabin

def test_factor_2_part():
    even_exponent = [0,1,123]
    odd_factor = [1,123,12345]
    for (k,q) in zip(even_exponent, odd_factor):
        assert factor_2_part((2**k) * q) == (k,q)

def test_miller_rabin_composite():
    N = 1234567*8910111213
    assert miller_rabin(N,15) == False

def test_miller_rabin_even_input():
    N = 2 * 1234567
    assert miller_rabin(N) == False
    
def test_miller_rabin_prime():
    p = 10000000019
    assert miller_rabin(p, 2) == True


test_factor_2_part()
test_miller_rabin_composite()
test_miller_rabin_even_input()
test_miller_rabin_prime()
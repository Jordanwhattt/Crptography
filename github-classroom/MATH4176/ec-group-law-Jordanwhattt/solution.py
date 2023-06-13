import math

def add(P,Q,A,B,p):
    """Returns P+Q on the curve y^2=x^3+Ax+b over Fp."""
    M=0
    if P == None:
        return Q
    if Q == None:
        return P
    xP = P[0]
    xQ = Q[0]
    yP = P[1]
    yQ = Q[1]
    if xP == xQ:
        if yP == pow(-yQ, 1, p):
            return None
        else:
            num = pow(3 * xP**2 + A, 1, p) 
            den = pow(2 * yP, -1, p)
            M =  pow(num * den, 1, p)   
    else:
        num = pow( (yP - yQ) , 1, p)
        den = pow( (xP - xQ) , -1, p)
        M =  pow(num * den, 1, p)   

    xR = pow(M**2 - xP - xQ, 1, p)
    yR = pow(M * (xP - xR) - yP, 1, p)
    p_plus_q = (xR, yR)
    return p_plus_q


def dbl(P,A,B,p):
    double = add(P, P, A, B, p)
    return double

def neg(P,p):
    """Returns -P on the curve y^2=x^3+Ax+b over Fp."""
    xP = P[0]
    yP = P[1]
    neg_yP = p - yP
    neg_P = (xP, neg_yP)
    return neg_P

def smul(n,P,A,B,p):
    """Returns nP on the curve y^2=x^3+Ax+b over Fp."""
    if n < 0:
        P = neg(P,p)
        n = abs(n)
    if n == 0:
        return 0
    elif n == 1:
        return P
    elif n % 2 == 1:
        return add(P, smul(n-1, P,  A, B, p), A, B, p)
    else:
        return smul(n // 2, dbl(P, A , B, p), A, B, p)

from fractions import Fraction
import random
from poly import *

# Multiplication f*g in Z[X]/(X^N - 1)
def ntrumul(f, g, N):
    """
    f = poly([2, 5])
    g = poly([4, 3])
    ntrumul(f, g, 3) == f*g % poly([-1, 0, 0, 1])
    >>> True

    where f*g % poly([-1, 0, 0, 1]) means f*g mod (X^3 - 1)
    """
    fg = []
    for j in range(N):
        s = 0
        for i in range(N):
            s = s + f[i]*g[(-i+j)%N]
        fg.append(s)
    return poly(fg)

def lift(x, p):
    """
    Function returns the polynomial 
    coefficients lie between -p/2 and p/2 (centered lift)

    lift(poly([1, 2, 3, 4, 5, 6]), 5)
    >>> poly([1, 2, -2, -1, 0, 1])
    """
    a = []
    for i in x:
        if i>p//2:
            a.append(i - p)
        else:
            a.append(i)
    return poly(a)

def L(d1, d2, N):
    """
    Function to create a polynomial degree N-1 that
    d1 coefficients equal 1, d2 coefficients equal -1, the rest 0.

    >>> L(1, 1, 5)
    poly([1, -1, 0, 0, 0])
    """

    l = [1]*d1 + [-1]*d2 + [0]*(N-d1-d2)
    out = []
    for i in range(N):
        j = random.randrange(0, N-i)
        out.append(l.pop(j))
    return poly(out)

# Function to generate the publickey
def genPublickey(f, g, N=5, p=3, q=128):
    fq = polyinv(f, poly([-1]+[0]*(N-1)+[1]))%q
    h = ntrumul(fq, g, N)%q
    return h

def enc(m, h, N=5, p=3, q=128):
    r = L(3, 3, 5)
    return (ntrumul(p*r, h, N) + m)%q

def dec(e, f, N=5, p=3, q=128):
    a = lift(ntrumul(f, e, N)%q, q)
    fp = polyinv(f, poly([-1]+[0]*(N-1)+[1]))%p
    return lift(ntrumul(fp, a, N)%p, p)

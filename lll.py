import math
import random
from fractions import Fraction
import numpy as np

# Gram-Schmidt Orthogonalization
def gram_schmidt(x):
    """
    >>> gram_schmidt([[3, 0], 
                      [-7, 1]])
    array([[3., 0.], 
           [0., 1.]])
    """
    dim = len(x)
    y = np.empty((0, dim))  
    for i in range(dim):
        t = np.array([0]*dim)
        for j in range(i):
            t = t + (np.dot(x[i], y[j])/np.dot(y[j], y[j]))*np.array(y[j])
        y = np.append(y, [x[i] - t], axis=0)
    return y

# LLL lattice basis reduction algorithm
def lll(x, delta=Fraction(1, 1)):
    """
    >>> lll([3, 0],
    ...     [-7, 1])
    array([[Fraction(-1, 1), Fraction(1, 1)],
           [Fraction(1, 1), Fraction(2, 1)]], dtype=object)
    """

    dim = len(x)
    b = np.array([[Fraction(x[i][j]) for j in range(dim)] for i in range(dim)])
    a = gram_schmidt(b)
    while(1):

        # Reduction Step
        y = np.append(np.empty((0, dim)), [b[0]], axis=0)
        for i in range(1, dim):
            for j in range(i-1, -1, -1):
                c = np.dot(b[i], a[j])/np.dot(a[j], a[j])
                b[i] = b[i] - c.__round__()*b[j]
            y = np.append(y, [b[i]], axis=0)            

        # Swap Step
        T = 1
        for i in range(dim-1):
            d = np.dot(b[i+1], a[i])/np.dot(a[i], a[i])

            # Check Lovasz Condition
            if delta.numerator*np.dot(a[i], a[i]) > delta.denominator*np.dot(a[i+1] + d*a[i], a[i+1] + d*a[i]):
                t = np.copy(b[i])
                b[i], b[i+1]= b[i+1], t
                a = gram_schmidt(b)
                T = 0
                break
        if T:
            break
    return y

# Function to make a NTRU Lattice
def nl(h, q):
    """
    h is a public key for NTRU Cryptosystem.
    The private key [f, g] is in NTRU Lattice
    [[I,  H], 
     [O, qI]],
    where H = cyclic permutations of the coefficients of h.

    >>> h = [1, 2, 3]
    >>> nl(h, 32)
    [[ 1,  0,  0,  1,  2,  3], 
     [ 0,  1,  0,  3,  1,  2], 
     [ 0,  0,  1,  2,  3,  1], 
     [ 0,  0,  0, 32,  0,  0],
     [ 0,  0,  0,  0, 32,  0],
     [ 0,  0,  0,  0,  0, 32]]
    """
    lh = len(h)
    out = [[h[(-i+j)%lh] for j in range(lh)] for i in range(lh)]
    for i in range(lh):
        I, I[i] = lh*[0], 1
        out[i] = I + out[i]
    for i in range(lh):
        Q, Q[i] = lh*[0], q
        out = out + [lh*[0] + Q]
    return out

def fracmat(x):
    return [[Fraction(x[i][j]) for j in range(len(x))] for i in range(len(x))]

def intmat(x):
    return [[int(x[i][j]) for j in range(len(x))] for i in range(len(x))]

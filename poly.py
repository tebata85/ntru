from fractions import Fraction

# Euclidean Algorithm for integer
def egcd(x, y):
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while y:
        q, r = x // y, x % y
        x, y = y, r
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
    gcd = x
    return gcd, a0, b0

# Modular inverse of an integer a mod m
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

# Modular of a fraction
def mod(a, m):
    if isinstance(a, int):
        return a % m
    gcd = egcd(a.denominator, m)[0]
    if gcd != 1:
        raise ZeroDivisionError
    else:
        return modinv(a.denominator, m)*a.numerator % m

# Multiplication of two polynomials
def polymul(f, g):
    degfg = len(f) + len(g)
    fg = []
    for k in range(degfg+1):
        c = 0
        for i in range(k+1):
            c = c + f[i]*g[k - i]
        fg.append(c)
    return fg

# Sum of two polynomials
def polyadd(f, g):
    degfg = max(len(f), len(g))
    fg = []
    for i in range(degfg+1):
        fg.append(f[i] + g[i])
    return fg

# Difference (subtraction) of two polynomials
def polysub(f, g):
    degfg = max(len(f), len(g))
    fg = []
    for i in range(degfg+1):
        fg.append(f[i] - g[i])
    return fg

# Returns the quotient and remainder of polynomial division
def polydiv(N, D):
    degD = len(D)
    if degD==0:
        return N*Fraction(1, D[0]), 0
    Q, r = poly([0]), N
    while len(r)>=degD:
        q = [0]*(len(r) - degD + 1)
        q[len(r) - degD] = Fraction((r[len(r)]) , D[degD])
        Q, r = Q + q, r - q*D
    return Q, r
 
def polymod(f, n):
    g = []
    for i in f:
        g.append(mod(i, n))
    return g

# Evaluate a polynomial at specific values
def polyval(p, x):
    y = 0
    for i in range(len(p)):
        y = y + p[i]*x**i
    return y

# Remove Leading Zeros
def trim(seq):
    if len(seq) == 0:
        return seq
    else:
        for i in range(len(seq) - 1, -1, -1):
            if seq[i] != 0:
               break
        return seq[0:i+1]

class poly(object):
    """
    poly([0, 3, 1]) means the polynomial x^2 + 3x

    >>> a = poly([0, 3, 1])
    >>> b = poly([1, 2])
    >>> a
    poly([0, 3, 1])

    Polynomials can be added, subtracted, multiplied, and divided
    (returns quotient and remainder):

    >>> a + b
    poly([1, 5, 1])

    >>> a*b
    poly([0, 3, 7, 2])

    >>> a/b
    (poly([5/4, 1/2]), poly([-5/4]))

    >>> a%b
    poly([-5/4])

    a to the 2 power
    >>> a**2
    poly([0, 0, 9, 6, 1])

    >>> a(3)
    18

    >>> a.rot(1)
    poly([1, 0, 3])

    >>> a<<2
    poly([0, 0, 0, 3, 1])
    """

    def __init__(self, seq):
        if isinstance(seq, poly):
            self.coef = seq.coef
            self.deg = seq.deg
        elif isinstance(seq, list):
            self.coef = trim(seq)
            self.deg = len(self.coef) - 1
        else:
            self.coef = [seq]
            self.deg = 0
    def __repr__(self):
        StrRepreObj = ''
        for i in self.coef:
            StrRepreObj = StrRepreObj + ', ' + str(i)
        return 'poly(['+StrRepreObj[2:]+'])'
    def __len__(self):
        return self.deg
    def __call__(self, val):
        return polyval(self.coef, val)
    def __getitem__(self, val):
        if val > self.deg:
            return 0
        if val < 0:
            return 0
        return self.coef[val]
    def __iter__(self):
        return iter(self.coef)
    def __neg__(self):
        return poly([-i for i in self])
    def __pos__(self):
        return self
    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            return poly([i*other for i in self.coef])
        else:
            return poly(polymul(self, poly(other)))
    def __rmul__(self, other):
        if isinstance(other, (int, Fraction)):
            return poly([other*i for i in self.coef])
        else:
            return poly(polymul(self, poly(other)))
    def __add__(self, other):
        return poly(polyadd(self, poly(other)))
    def __radd__(self, other):
        return poly(polyadd(self, poly(other)))
    def __pow__(self, val):
        if not isinstance(val, int) or int(val) != val or val < 0:
            raise ValueError("Power to non-negative integers only.")
        res = poly([1])
        for _ in range(val):
            res = self*res
        return poly(res)
    def __sub__(self, other):
        return poly(polysub(self, poly(other)))
    def __rsub__(self, other):
        return poly(polysub(poly(other), self))
    def __div__(self, other):
        if isinstance(other, (int, Fraction)):
            return self*Fraction(1, other)
        else:
            return polydiv(self, poly(other))
    __truediv__ = __div__
    def __rdiv__(self, other):
        if isinstance(other, (int, Fraction)):
            return Fraction(other)*self
        else:
            return polydiv(poly(other), self)
    __rtruediv__ = __rdiv__
    def __mod__(self, other):
        if isinstance(other, int):
            return poly(polymod(self, other))
        return (self / other)[1]
    def __lshift__(self, other):
        """
        >>> poly([2, 3])<<2
        poly([0, 0, 2, 3])
        """
        return (self*([0]*other + [1]))
    def __eq__(self, other):
        if isinstance(other, int):
            return self.coef == [other]
        if not isinstance(other, poly):
            return NotImplemented
        return self.coef == other.coef
    def __ne__(self, other):
        if not isinstance(other, poly):
            return NotImplemented
        return not self.__eq__(other)
    def rot(f, n):
        lh = len(f) + 1
        return poly([f.coef[(-n+j)%lh] for j in range(lh)])

# Euclidean Algorithm for polynomials
def pgcd(x, y):
    a0, a1 = 1, 0
    b0, b1 = 0, 1
    while len(y):
        q, r = x / y        
        x, y = y, r
        a0, a1 = a1, (a0 - q * a1)
        b0, b1 = b1, (b0 - q * b1)
    x, y = y, r
    a0, a1 = a1, (a0 - q * a1)
    b0, b1 = b1, (b0 - q * b1)
    if len(x) == 0:
        a0 = Fraction(1, x[0])*a0
        b0 = Fraction(1, x[0])*b0
        x = poly([1])
    return x, a0, b0

# Inverse of a polynomial a in Z[X]/m
def polyinv(a, m):
    gcd, x, y = pgcd(a, m)
    if gcd != poly(1):
        return None
    else:
        return x % m

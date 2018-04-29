from lll import *
from ntru import *

"""
Ntru parameters: (N, p, q) = (5, 3, 128)
Private key: f = x^4 + x^3 - 1 = poly([-1, 0, 0, 1, 1])
             g = x^3 - x = poly([0, -1, 0, 1])
Message : m = -x^4 + x^2 + x - 1

"""

# NTRU parameter
(N, p, q) = (5, 3, 128)
print('Parameters  :  (N, p, q) = ', (N, p, q))

# Private key
f = poly([-1, 0, 0, 1, 1])
g = poly([0, -1, 0, 1])
print('PrivateKey f: ', f)
print('PrivateKey g: ', g)

# Public key
h = genPublickey(f, g, N, p, q)
print('PublicKey  h: ', h, ' ( = genPublickey(f, g))')

# Message
m = poly([-1, 1, 1, 0, -1])
print('PlainText  m: ', m)

# Encryption
e = enc(m, h, N, p, q)
print('Ciphertext e: ', e, ' ( = enc(m, h))')

#Decryption
print('Decryption  : ', dec(e, f, N, p, q), ' ( = dec(e, f))')
print('>>> dec(m, f) == m')
print(dec(m, f) == m)

#Lattice attack
print('-----------------Lattice Attack----------------------')
print('The vector [f, g] is in the NTRU lattice ')
NTRULattice = nl(h.coef, q)
print(np.array(NTRULattice))

print('Aplying LLL to NTRU Lattice ')
Lh = intmat(lll(NTRULattice))
print(np.array(Lh))

print('The first row vector [F, G]: ')
F, G = Lh[0][:len(Lh)//2], Lh[0][len(Lh)//2:]
print('F, G = ', F, G)

print('Decrypt massege')
print('>>> dec(m, poly(F))')
print(dec(m, poly(F)))
print('>>> dec(m, poly(F)) == m')
print(dec(m, poly(F)) == m)

for i in range(len(h)+1):
    if f == poly(F).rot(i):
        sign = 1
        break
    if f == -poly(F).rot(i):
        sign = -1
        break
print('Rotation of F is equal to private key f')
print('f = ', sign, '*x^', i, '*F')

if __name__ == '__main__':
    import code
    console = code.InteractiveConsole(locals=locals())
    console.interact()
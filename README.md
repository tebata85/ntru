# Lattice Attack on NTRU (Python 3.5)

A Python implementation of the NTRU public key cryptosystem and a Lattice Attack on NTRU.
NTRU was first suggested by Jeffrey Hoffstein, Jill Pipher, Joseph H. Silvermam in the 
rump session of CRYPTO'96', and was published in 1) in 1998. It is based on the shortest 
vector problem in a lattice (which is not known to be breakable using quantum computers.)
LLL lattice basis reduction algorithm 2) calculates an LLL-reduced bases in polynomial time.
The first vector of LLL-reduced basis is approximate solution of the shortest vector problem.

The ntru package includes:

* poly.py: Polynomial library

* ntru.py: NTRU Cryptosystem

* lll.py: LLL lattice basis reduction algorithm using Numpy


# Refferences

1) Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman 
NTRU: A Ring Based Public Key Cryptosystem. In Algorithmic Number Theory (ANTS III), 
Portland, OR, June 1998, J.P. Buhler (ed.), Lecture Notes in Computer Science 1423, 
Springer-Verlag, Berlin, 1998, 267-288

2) A. K. Lenstra, H. W. Lenstra, Jr., L. Lovasz Factoring, polynomials with rational
coefficients, Mathematische Annalen, 261 (1982), pp. 513–534.

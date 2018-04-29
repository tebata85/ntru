# NTRUへの格子攻撃（Python 3.5）

PythonによるNTRU公開鍵暗号システムとNTRUへの格子攻撃の実装。
NTRUはJeffrey Hoffstein、Jill Pipher、Joseph H. Silvermam によってCRYPTO'96 'の
rump sessionで最初に提案され1998年に 1）で公開されました。これは格子の最短ベクトル問題
（量子コンピュータを用いた解読方法は知られていない）に基づいています。
LLL格子基底縮小アルゴリズム 2）は多項式時間でLLL縮小基底を計算する。
LLL縮小基底の最初のベクトルは、最短ベクトル問題の近似解となります。

パッケージ:

* poly.py: 多項式ライブラリ

* ntru.py: NTRU暗号

* lll.py: Numpyを用いたLLL格子基底縮小アルゴリズム

# 参考文献

1) Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman 
NTRU: A Ring Based Public Key Cryptosystem. In Algorithmic Number Theory (ANTS III), 
Portland, OR, June 1998, J.P. Buhler (ed.), Lecture Notes in Computer Science 1423, 
Springer-Verlag, Berlin, 1998, 267-288

2) A. K. Lenstra, H. W. Lenstra, Jr., L. Lovasz Factoring, polynomials with rational
coefficients, Mathematische Annalen, 261 (1982), pp. 513–534.
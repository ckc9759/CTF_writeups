### Akasec ctf writeups

---

#### lost - crypto

```py

from random import getrandbits
from Crypto.Util.number import getPrime, bytes_to_long
from SECRET import FLAG

e = 2
p = getPrime(256)
q = getPrime(256)
n = p * q

m = bytes_to_long(FLAG)
cor_m = m - getrandbits(160)

if __name__ == "__main__":
    c = pow(m, e, n)
    print("n = {}\nc = {}\ncor_m = {}".format(n, c, cor_m))
```

We see `e` is small, first we try for weiner's attack of small exponent but it fails. Then we make use of `cor_m` which is partial m (change to bytes to see partial flag).
When we know the partial message, we can apply `Coppersmith attack`. Did a bit researching and came out with this.

```py
m=724154397787031699242933363312913323086319394176220093419616667612889538090840511506381320998293481458429167685676367015744314015744
n=5113166966960118603250666870544315753374750136060769465485822149528706374700934720443689630473991177661169179462100732951725871457633686010946951736764639
e=2
c=329402637167950119278220170950190680807120980712143610290182242567212843996710001488280098771626903975534140478814872389359418514658167263670496584963653
P.<x> = PolynomialRing(Zmod(n), implementation='NTL')
pol = (m + x)^e - c
roots = pol.small_roots(epsilon=1/50)
print("Potential solutions:")
for root in roots:
      a = root+m
      print(root+m)
      #print(long_to_bytes(a))
      #print(long_to_bytes(root))
#AKASEC{c0pp3r5m17h_4774ck_1n_1ov3_w17h_5m4ll_3xp0n3nts}
```

---

#### twins - crypto

```py
#chall.py
from Crypto.Util.number import getPrime, bytes_to_long
from SECRET import FLAG

e = 5
p = getPrime(256)
q = getPrime(256)
n = p * q

m1 = bytes_to_long(FLAG)
m2 = m1 >> 8

if __name__ == "__main__":
    c1, c2 = pow(m1, e, n), pow(m2, e, n)
    print("n = {}\nc1 = {}\nc2 = {}".format(n, c1, c2))
```

We see `e` is small again, so we can try weiner's attack but again it fails, factordb also didn't give p,q. 
So, we try to make use of m2 given, a bit googling revealed that the given condition fits for `related message RSA attack` or `franklin reiter attack`

```py
e=5

n = 6689395968128828819066313568755352659933786163958960509093076953387786003094796620023245908431378798689402141767913187865481890531897380982752646248371131
c1 = 3179086897466915481381271626207192941491642866779832228649829433228467288272857233211003674026630320370606056763863577418383068472502537763155844909495261
c2 = 6092690907728422411002652306266695413630015459295863614266882891010434275671526748292477694364341702119123311030726985363936486558916833174742155473021704
n1=n
n2=n

def my_gcd(a, b): 
    return a.monic() if b == 0 else my_gcd(b, a % b)

R.<m2>=Zmod(n)[]
for k in range(256):
   f1=(m2*256+k)^e-c1
   f2=m2^e-c2
   print(-my_gcd(f1, f2).coefficients()[0])
#AKASEC{be_on_the_right_side_of_history_free_palestine}
```

---

#### My calculus lab - crypto

```py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import hashlib
import sympy as sp
import random

FLAG = b'REDACTED'
key = random.getrandbits(7)
x = sp.symbols('x')
f = "REDACTED"
f_prime = "REDACTED"
f_second_prime = "REDACTED"

assert(2*f_second_prime - 6*f_prime + 3*f == 0)
assert(f.subs(x, 0) | f_prime.subs(x, 0) == 14)

def encrypt(message, key):
    global f
    global x
    point = f.subs(x, key).evalf(100)
    point_hash = hashlib.sha256(str(point).encode()).digest()[:16]
    cipher = AES.new(point_hash, AES.MODE_CBC)
    iv = cipher.iv
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    return iv.hex() + ciphertext.hex()

encrypted = encrypt(FLAG, key)

print(f"Key: {key}")
print(f"Encrypted: {encrypted}")
```

The given question is a basic AES encryption where the point hash is used to encrypt the message. If we find the point being used, then we can easily decrypt the message as `iv` is also known.
To find the point, we need to solve the double differential equation and then substitute the initial conditions. Tried manually but the second bitwise condition has bunch of possible answers.
So, I used a script to find all the possible answers.

```py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import hashlib
import sympy as sp
import random
import math
from sympy import symbols, Function, Eq, dsolve, exp, Derivative

x = sp.symbols('x')
e=math.e
Key=60
Encrypted='805534c14e694348a67da0d75165623cf603c2a98405b34fe3ba8752ce24f5040c39873ec2150a61591b233490449b8b7bedaf83aa9d4b57d6469cd3f78fdf55'

iv_hex=Encrypted[:32]
ct=Encrypted[32:]

iv=bytes.fromhex(iv_hex)
c=bytes.fromhex(ct)
print(iv)
print(c)

pos14=[[0, 14], [2, 12], [2, 14], [4, 10], [4, 14], [6, 8], [6, 10], [6, 12], [6, 14], [8, 6], [8, 14], [10, 4], [10, 6], [10, 12], [10, 14], [12, 2], [12, 6], [12, 10], [12, 14], [14, 0], [14, 2], [14, 4], [14, 6], [14, 8], [14, 10], [14, 12], [14, 14]]

x = symbols('x')
y = Function('y')(x)

# Define the differential equation 2y''-6y'+3y=0
differential_eq = Eq(2*y.diff(x, x) - 6*y.diff(x) + 3*y, 0)

for i in range(len(pos14)):
   # Define initial conditions y(0) = y0 and y'(0) = y1
   y0 = pos14[i][0]  # Ey(x)
   y1 = pos14[i][1]  # y'(x)
   initial_conditions = {y.subs(x, 0): y0, y.diff(x).subs(x, 0): y1}
   # Solve the differential equation with initial conditions
   solution = dsolve(differential_eq, y, ics=initial_conditions)
   f=solution.rhs
   point = f.subs(x, Key).evalf(100)
   #print(point)
   point_hash = hashlib.sha256(str(point).encode()).digest()[:16]
   cipher = AES.new(point_hash, AES.MODE_CBC, iv)
   flag = cipher.decrypt(c)
   print(flag)

#pos14 is the possible two numbers with bitwise OR having 14
#AKASEC{d1d_y0u_3nj0y_c41cu1u5_101?}
```

---

#### pyjail - misc

```py
import sys
from string import printable

print('''
#################################################################
#                                                               #
#   Welcome to pyJail!                                          #
#                                                               #
#   You have been jailed for using too many characters.         #
#                                                               #
#   You are only allowed to use 16 characters of printable      #
#   ascii.                                                      #
#                                                               #
#   If you manage to break free, you will get the flag.         #
#                                                               #
#################################################################\n''')

code = input('> ')

sys.stdin = None

len = sum(1 for char in code if char in printable)

if len >= 17:
    print('Too long!')
    exit()

eval(code)
```

We can see the length of code we can specify is 16 max, but since only printable is check, we can bypass the ascii letters with italics.
`__import__('os')` this works without error, so it means nothing is blacklisted (evident from code too).

Using italics or bold, the only thing which is getting counted is `.`,`(`,`'`,`_` and other special characters. So if we try to import a module and then use it, it's going to cost
more than 16. Therefore, we make use of the already imported `sys` module to cat the flag.
`𝘴𝘺𝘴.𝘮𝘰𝘥𝘶𝘭𝘦𝘴['os'].𝘴𝘺𝘴𝘵𝘦𝘮('ls')` this is a working payload with 15 length, if we try replacing `ls` with `cat flag.txt`, it's going beyond the prescribed limit.
Hence, we call `sh` to enter a shell on the server and the we can cat the flag. `ls` and `os` have to be normal strings otherwise python won't recognise them.

`𝘴𝘺𝘴.𝘮𝘰𝘥𝘶𝘭𝘦𝘴['os'].𝘴𝘺𝘴𝘵𝘦𝘮('sh')` --> `AKASEC{1t5_4ll_4b0ut_3sc4p1ng_4nd_3v4lu4T1ng}`

---

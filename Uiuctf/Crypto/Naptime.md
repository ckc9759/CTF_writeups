### Naptime

---
<br />

> ## Description:
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/e83fe43a-1f7f-4dd5-a14b-aeffa05ab036)

We're given two files.
<br />

> ## Attachments:

```py
#pub.txt
a =  [66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]
ct = [273896, 179019, 273896, 247527, 208558, 227481, 328334, 179019, 336714, 292819, 102108, 208558, 336714, 312723, 158973, 208700, 208700, 163266, 244215, 336714, 312723, 102108, 336714, 142107, 336714, 167446, 251565, 227481, 296857, 336714, 208558, 113681, 251565, 336714, 227481, 158973, 147400, 292819, 289507]
```

```py
#enc_dist.sage
from random import randint
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import numpy as np

def get_b(n):
    b = []
    b.append(randint(2**(n-1), 2**n))
    for i in range(n - 1):
        lb = sum(b)
        found = False
        while not found:
            num = randint(max(2**(n + i), lb + 1), 2**(n + i + 1))
            if num > lb:
                found = True
                b.append(num)

    return b

def get_MW(b):
    lb = sum(b)
    M = randint(lb + 1, 2*lb)
    W = getPrime(int(1.5*len(b)))

    return M, W

def get_a(b, M, W):
    a_ = []
    for num in b:
        a_.append(num * W % M)
    pi = np.random.permutation(list(i for i in range(len(b)))).tolist()
    a = [a_[pi[i]] for i in range(len(b))]
    return a, pi


def enc(flag, a, n):
    bitstrings = []
    for c in flag:
        # c -> int -> 8-bit binary string
        bitstrings.append(bin(ord(c))[2:].zfill(8))
    ct = []
    for bits in bitstrings:
        curr = 0
        for i, b in enumerate(bits):
            if b == "1":
                curr += a[i]
        ct.append(curr)

    return ct

def dec(ct, a, b, pi, M, W, n):
    # construct inverse permuation to pi
    pii = np.argsort(pi).tolist()
    m = ""
    U = pow(W, -1, M)
    ct = [c * U % M for c in ct]
    for c in ct:
        # find b_pi(j)
        diff = 0
        bits = ["0" for _ in range(n)]
        for i in reversed(range(n)):
            if c - diff > sum(b[:i]):
                diff += b[i]
                bits[pii[i]] = "1"
        # convert bits to character
        m += chr(int("".join(bits), base=2))

    return m


def main():
    flag = 'uiuctf{I_DID_NOT_LEAVE_THE_FLAG_THIS_TIME}'

    # generate cryptosystem
    n = 8
    b = get_b(n)
    M, W = get_MW(b)
    a, pi = get_a(b, M, W)

    # encrypt
    ct = enc(flag, a, n)

    # public information
    print(f"{a =  }")
    print(f"{ct = }")

    # decrypt
    res = dec(ct, a, b, pi, M, W, n)

if __name__ == "__main__":
    main()

'''Analyzing the code and the given public key, we can observe it's performing some kind of encryption. After searching on google and with chatGPT for a while, it comes out to be
`Merkle-Hellman knapsack cryptosystem` '''.
```
<br />

> ## Approach:

**Merkle-Hellman knapsack cryptosystem** is an old cryptosystem which already has been broken. We've the public key with us and we need to figure out the plaintext from that. My first approach was
to find the parameters `b`, `pi`, `M`, `W` but it can't be found in linear time so I left that approach.

I read the whole [GFG](https://www.geeksforgeeks.org/knapsack-encryption-algorithm-in-cryptography/) document for understanding the cryptosystem. It takes a flag or plaintext as a binary string of
length `n` (in our case it's 8), it generates a superincreasing list `b` of size `n`. The implementation of `get_b(n)` function shows that every entry in the list is within 2**k, 2**(k+1) range for some k.
Then it generates a random permutation `pi` of length `n` from numbers (0,n-1) and also generates modulus `M` and multiplier `W` which are used to generate `a` such that it's harder to reverse the
operations to find b. ( Involves modular arithmetics ).

I searched for `merkle hellman attack implementation` and got this GitHub [repo](https://github.com/taniayu/merklehellman-lll-attack). It implements the `lll` attack on Merkle.
I cloned the github in my system and supplied the public keys in the `tester.py` which reveals the flag.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/75b35b3b-31df-4ecc-8f1b-0b6938267cf5)

I tried this initially as well but it failed as I need to decrypt every block of cipher individually and then concatenate it.
<br />

> ## Final Solve:

```py
#tester.py
import time
from random import choice
import string
import util
from encryption import *
from decryption import *
from attacker import *

def test_attack(text):
    temp=[]
    pub=[66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]
    ct=[273896, 179019, 273896, 247527, 208558, 227481, 328334, 179019, 336714, 292819, 102108, 208558, 336714, 312723, 158973, 208700, 208700, 163266, 244215, 336714, 312723, 102108, 336714, 142107, 336714, 167446, 251565, 227481, 296857, 336714, 208558, 113681, 251565, 336714, 227481, 158973, 147400, 292819, 289507]
    for i in range(len(ct)):
       cracked = crack_ciphertext(pub, ct[i])
       #print cracked
       temp.append(cracked)
    print(temp)
    print ''.join(temp)
    return 1

test_attack('Hello')

test_attack('Hello') # Any random string as we're not testing the attack script but supplying our public keys
```

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/1e19c498-7b2a-4d1b-bf34-509ef41a007b)

#### Final flag : uiuctf{i_g0t_sleepy_s0_I_13f7_th3_fl4g}
<br />

> ## Alternate approach:

Alternatively, we can just bruteforce the flag with a character set. We know the flag is formed from ascii characters, we encrypt every character in `n` bits binary string format and check if the encyption matches our
ciphertext `ct1`, if it matches, the character at that particular index is correct so we concatenate it !

```py
#bf.py
import string
flag=string.printable

a =  [66128, 61158, 36912, 65196, 15611, 45292, 84119, 65338]
ct1 = [273896, 179019, 273896, 247527, 208558, 227481, 328334, 179019, 336714, 292819, 102108, 208558, 336714, 312723, 158973, 208700, 208700, 163266, 244215, 336714, 312723, 102108, 336714, 142107, 336714, 167446, 251565, 227481, 296857, 336714, 208558, 113681, 251565, 336714, 227481, 158973, 147400, 292819, 289507]

bitstrings = []
for c in flag:
    bitstrings.append(bin(ord(c))[2:].zfill(8))

ct = []
for bits in bitstrings:
    curr = 0
    for i, b in enumerate(bits):
            if b == "1":
                    curr += a[i]
    ct.append(curr)

pt = ""
for t in ct1:
    i = ct.index(t)
    pt += flag[i]

print(pt)
#uiuctf{i_g0t_sleepy_s0_I_13f7_th3_fl4g}
```

---

#### Resources referred

[Archaic from ASIS CTF](https://ctftime.org/writeup/2236)  
[Knapsack Cipher](https://ctf-wiki.mahaloz.re/crypto/asymmetric/knapsack/knapsack/)  
[Wiki](https://en.wikipedia.org/wiki/Merkle%E2%80%93Hellman_knapsack_cryptosystem)  
[Auctf 2020](https://jsur.in/posts/2020-04-06-auctf-2020-writeups/)  
[LLL Algo](https://mathweb.ucsd.edu/~crypto/Projects/JenniferBakker/Math187/)
[Dante CTF](https://meashiri.github.io/ctf-writeups/posts/202306-dantectf/#adventurers-knapsack)
[Crypto stack exchange](https://crypto.stackexchange.com/questions/50068/how-to-attack-merkle-hellman-cryptosystem-if-the-first-element-in-the-superincre)

Thank you  
***ckc9759***



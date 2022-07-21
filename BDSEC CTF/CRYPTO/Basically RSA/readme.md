### Chall Desc : 

RSA cryptosystem uses modular arithmetic to create an asymmetric encryption system. However, there are some pitfalls and weakness. Can you exploit it?

```py
N: 1280678415822214057864524798453297819181910621573945477544758171055968245116423923

E: 65537

C: 241757357533719849989659127349827982677055294256023833052829147857534659015212862
```

Flag Format : BDSEC{fl4g_h3r3}

### File attached : none

### Soln :

It is a simple RSA problem.

Script : 

```py
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ python3
Python 3.8.10 (default, Mar 15 2022, 12:22:08)
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from Crypto.Util.number import *
>>> n=1280678415822214057864524798453297819181910621573945477544758171055968245116423923
>>> e=65537
>>> c=241757357533719849989659127349827982677055294256023833052829147857534659015212862
>>> p=1899107986527483535344517113948531328331
>>> q=674357869540600933870145899564746495319033
>>> phi=(p-1)*(q-1)
>>> d=inverse(e,phi)
>>> m=pow(c,d,n)
>>> print(long_to_bytes(m))
b'BDSEC{r54_i5_fUn_r16h7?}'
```

### THE FLAG : BDSEC{r54_i5_fUn_r16h7?}

---

Thank you

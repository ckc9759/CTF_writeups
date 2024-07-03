### X Marked the Spot

---
<br />

> ## Description:
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/dde3c728-eb89-420f-a0bc-9b19dde4b476)

This seems to be a beginner level challenge as mentioned from the description, we're provided two files.

<br />

> ## Attachments:
```py
public.py
from itertools import cycle

flag = b"uiuctf{????????????????????????????????????????}"
# len(flag) = 48
key  = b"????????"
# len(key) = 8
ct = bytes(x ^ y for x, y in zip(flag, cycle(key)))

with open("ct", "wb") as ct_file:
    ct_file.write(ct)
```

```py
#ct
X6.
   Z.^;
       9^]T6
U5BHPCGK
```

<br />

> ## Approach:
It looks like our flag is xored with a key of length 8. `ct = bytes(x ^ y for x, y in zip(flag, cycle(key)))`
Since XOR operation is reversible, We need to find the key to xor the ciphertext and get back our flag (plaintext).

Flag format in the ctf was `uiuctf{` which is 7 character long, hence we can find the key upto length 7 and then we need to bruteforce.

We open our file `ct` in bytes format `rb` and xor it with b'uiuctf{' (`known plaintext attack`)

<br />

> ## Final Solve:
```py
from itertools import cycle
import string

f=open('ct','rb').read()
print(f'{f=}')
key=b'uiuctf{'
pt=bytes(x ^ y for x, y in zip(f, cycle(key)))
key=pt[:7]
temp=string.printable

#bf for the last key character
for tt in temp:
    k=key
    k=k+tt.encode()
    pt=bytes(x ^ y for x, y in zip(f, cycle(k)))
    if pt.endswith(b'}'):
        print(f'{key=}')
        print(f'{pt=}')
```

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/d1d88c6e-6749-4223-b79d-1f48e3e430e4)

Hence,

#### Flag : uiuctf{n0t_ju5t_th3_st4rt_but_4l50_th3_3nd!!!!!}

---

Thank you  
***ckc9759***

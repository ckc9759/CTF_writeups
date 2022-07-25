### Chall Desc : 
The unbreakable one byte pad

### File attached :
[encrypt.py](enc.py)
[output.txt](out.txt)

#### Soln :

We try to understand the encoding steps :

```py
import random

with open('flag.txt', 'rb') as f:
    plaintext = f.read()

key = random.randrange(256)
ciphertext = [key ^ byte for byte in plaintext]

with open('output.txt', 'w') as f:
    f.write(bytes(ciphertext).hex())
```

In this python code, we have take a random key and used it to xor our plain text to get the ciphertext.

We know xor property that a xor b is c and we can get a back using c xor b.

Therefore if a is plaintext flag and c is ciphertext flag and b is the xor key value, we can retrieve back our flag.

I used dcode.fr to brute force for the xor key and got the flag.

#### THE FLAG : hope{not_a_lot_of_keys_mdpxuqlcpmegqu}

---

Thank you

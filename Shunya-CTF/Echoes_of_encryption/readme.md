### Echoes of encryption

---

The encryption script is secure only coz of seed. random.choice won't be random if we seed the random with a value.

```py
#encrypt function
def encrypt_string(input_string, seed):
    random.seed(seed)
    allowed_chars = string.ascii_letters + string.digits
    key = ''.join(random.choices(allowed_chars, k=len(input_string)))
    encrypted_string = ''
    for i in range(len(input_string)):
        encrypted_char = chr(ord(input_string[i]) ^ ord(key[i]))
        encrypted_string += encrypted_char
    return encrypted_string.encode().hex()
```

Bruteforcing doesn't work as seed is very large. 

Seed value was in the CVE December of Nvidia vuln as mentioned in desc.
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/94d0225a-a08d-4cd5-bbc6-9cd9b6a3ca89)

#### Solution script

```py
import random
import string
import binascii

def dec(enc):
        dec = ''
        for i in range(0, len(enc), 2):
            byte = int(enc[i:i+2], 16)
            random.seed(202242269)
            allowed_chars = string.ascii_letters + string.digits
            key = ''.join(random.choices(allowed_chars, k=len(enc) // 2))
            decrypted_char = chr(byte ^ ord(key[i // 2]))
            dec += decrypted_char
        print(f"Decrypted String: {dec}")

key=''
data=b'OCTF{'
enc = "5e04610a22042638723c571e1a5436142764061f39176b4414204636251072220a35583a60234d2d28082b"
enc2=binascii.unhexlify(enc)
print(len(enc2[:5]))


for b1,b2 in zip(data,enc2[:5]):
   key+=chr(b1^b2)

print(key)
allowed_chars = string.ascii_letters + string.digits
print(allowed_chars)
'''
for i in range(193295,10000000000000000000000):
   random.seed(i)
   key = ''.join(random.choices(allowed_chars, k=43))
   if key.startswith('G5LY'):
      print(key)
      print(i)
      break
   else:
      print(f"NO {i}")
            '''
dec(enc)
```
Decrypted String: 0CTF{alw4y5_r3ad_7he_d3scr!pti0n_c4r3fully}

### Chall Desc: 
I'm carefully drawing a fine line on this piece of paper, letting each portion guide the next...  
(Digits and letters are 0-9 and 10-35 in their usual orders, and the underscore is 36.  
{} are not encoded but should be added in afterwards. All letters are lowercase.)

Hint 1 of 2
This uses the affine cipher, as clued by the title and description, but with an added modification.

Hint 2 of 2
Each pair of letters decodes the next.

### File content:
`(bc)bx6ez_unufi3bm0r0xeb`

### Soln:

> Another Straight forward question. It is `affine cipher` involving modular arithmetics, also hinted by chall name.  

The tricky part to it is, every pair of 2 characters act as a key to the next two characters.  

Since it uses the above format to encrypt, we know that the first 2 charcters will be bc and wont be encrypted.

Affine Cipher follows y = (a*x + b) mod m where y is the ciphertext and x is the plaintext. 

Since we know the domain of all characters used, we can say m = 36. And since the first 2 characters are b and c, we can assume `a = ord('b')`and ` = ord('c')`
Once we get these , we can continually decrypt pairs of ciphertext to get every pair of plaintext by using the affine decryption method ` x = ( (y-c) * a_inv) mod m`.

Python Script:   

```py
from Crypto.Util.number import *
plaintext = "bc"
ciphertext = "bx6ez_unufi3bm0r0xeb"
mapping = list("0123456789abcdefghijklmnopqrstuvwxyz_")
# affine cipher is (ax+b)modm = c
m = len(mapping)
for i in range(0,len(ciphertext),2):
    ciphertexts = (ciphertext[i],ciphertext[i+1])
    a = mapping.index(plaintext[-2])
    b = mapping.index(plaintext[-1])
    for c in ciphertexts:
        p = ((mapping.index(c)-b)%m*inverse(a,m))%m
        plaintext+= mapping[p]
print(plaintext)
```

Thank you

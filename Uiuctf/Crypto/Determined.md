### Determined

---
<br />

> ## Description:

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/4984f183-ea8a-469c-80ea-d77b9dc89370)

This looks like a matrix based cryptography question.

We're given 3 files here.  
<br />

> ## Attachments:

```py
#server.py
from Crypto.Util.number import bytes_to_long, long_to_bytes
from itertools import permutations
from SECRET import FLAG, p, q, r



def inputs():
    print("[DET] First things first, gimme some numbers:")
    M = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    try:
        M[0][0] = p
        M[0][2] = int(input("[DET] M[0][2] = "))
        M[0][4] = int(input("[DET] M[0][4] = "))

        M[1][1] = int(input("[DET] M[1][1] = "))
        M[1][3] = int(input("[DET] M[1][3] = "))

        M[2][0] = int(input("[DET] M[2][0] = "))
        M[2][2] = int(input("[DET] M[2][2] = "))
        M[2][4] = int(input("[DET] M[2][4] = "))

        M[3][1] = q
        M[3][3] = r

        M[4][0] = int(input("[DET] M[4][0] = "))
        M[4][2] = int(input("[DET] M[4][2] = "))
    except:
        return None
    return M

def handler(signum, frame):
    raise Exception("[DET] You're trying too hard, try something simpler")

def fun(M):
    def sign(sigma):
        l = 0
        for i in range(5):
            for j in range(i + 1, 5):
                if sigma[i] > sigma[j]:
                    l += 1
        return (-1)**l

    res = 0
    for sigma in permutations([0,1,2,3,4]):
        curr = 1
        for i in range(5):
            curr *= M[sigma[i]][i]
        res += sign(sigma) * curr
    return res

def main():
    print("[DET] Welcome")
    M = inputs()
    if M is None:
        print("[DET] You tried something weird...")
        return

    res = fun(M)
    print(f"[DET] Have fun: {res}")

if __name__ == "__main__":
    main()
```

```py
#gen.py
from SECRET import FLAG, p, q, r
from Crypto.Util.number import bytes_to_long
n = p * q
e = 65535
m = bytes_to_long(FLAG)
c = pow(m, e, n)
# printed to gen.txt
print(f"{n = }")
print(f"{e = }")
print(f"{c = }")
```

```py
#gen.txt
n = 158794636700752922781275926476194117856757725604680390949164778150869764326023702391967976086363365534718230514141547968577753309521188288428236024251993839560087229636799779157903650823700424848036276986652311165197569877428810358366358203174595667453056843209344115949077094799081260298678936223331932826351
e = 65535
c = 72186625991702159773441286864850566837138114624570350089877959520356759693054091827950124758916323653021925443200239303328819702117245200182521971965172749321771266746783797202515535351816124885833031875091162736190721470393029924557370228547165074694258453101355875242872797209141366404264775972151904835111
```
<br />

> ## Approach:

It is a `RSA` question and we're given the public keys `n`,`e` with the ciphertext `c`. I tried `factordb` as well as `ecm` of sage cell to factor n but both of them failed.
I then started looking at the `server.py`.

The `server.py` takes few inputs from the user, stores it in the initialized matrix M, the `fun` function then multiplies `curr` with few matrix entries and then adds them up and returns as variable `res`.
The `sign` function returns 1 or -1 depending upon the nested loop check `if sigma[i] > sigma[j]:`.

The key thing to notice here is,
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/6207bb42-8db5-4f34-8ec4-74f8ae312b5c)

The public keys `p` and `q` are also a part of our Matrix `M`. If we can somehow calculate even 1 of them, RSA is cracked !!
I altered parts of code to see the output, for test purpose, I took p=11,q=22,r=33.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/fe899b28-e6a0-45a2-8ea7-f339391c3d28)

I printed all the current values in every iteration when all the entries supplied to the server.py was 1s.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/3ea9d593-8678-4c79-adb8-d5a6220bb186)
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/d4e5f5ac-915a-4efa-aa5d-f4f2e8551bba)

I found that apart from few initial operations, the test value `q` was leaked quite often and sometimes `r`. It still required quite computation if we needed to calculate q.
I got this hint from description `shortened by 50% if one throws the matrices out.` and then I thought of cancelling few more rows with the help of 0s such that I can isolate the q (as it was leaked towards the end).

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/f7c08c86-4fdb-4fcc-80f2-2a8c0a3d395c)

<br />

> ## Final Solve:
If we visualize our matrix, we can see that it's possible to get the q isolated if the right diagonal entries are 1s and rest are 0s.
Hence, the optimal input to server would be `0,1,0,1,0,1,0,1,0` which can be matched with the matrix indices, all entries become zero except the last one and hence, q can be extracted.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/4b854ca8-a952-44c5-9a13-376bd082d355)

Refer to this [Script](https://github.com/ckc9759/CTF_resources/blob/main/CRYPTO/RSA/Different%20attacks/Known%20factors%20attack/readme.md) which works when a factor of RSA is known !

#### Flag : uiuctf{h4rd_w0rk_&&_d3t3rm1n4t10n}

---

Thank you  
***ckc9759***



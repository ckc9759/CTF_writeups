### Chall Desc : VE -RSA - TILE

```py
We found a file on the attacker's computer, but it seems to be encrypted with some kind of algorithm.
Nevertheless, we believe the attacker made a fatal mistake when choosing the factors...

Prompt: Can you decrypt the message and find the flag?

Flag format: IGE{XXXXXX_XXXXX_XXXX_XXXXXXX}

Credit: Christoph T.
```

---

### Soln : 

It was a standard RSA question and could be solved using a script or a decoder online like dcode.fr or Boxentriq.

The method can be found in the RSA folder of CTF resources in my github profile.

Basic idea is we have a N which is made of two primes p and q.

We are given the public key e and we need to find d to decrypt our message m.

So we find p and q, then calculate phi using (p-1)*(q-1),

then we calculate d using inverse of e,phi.

Then we can find out the message using :

```py
m=pow(c,d,n)
```

#### THE FLAG : IGE{4lw4ys_ch3ck_y0ur_pr1m3s!}

---
Thank you


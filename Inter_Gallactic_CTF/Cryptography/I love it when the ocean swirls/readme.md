### Chall Desc : I love it when the ocean swirls

```py
Scenario:

While the forensics team was looking through a confiscated computer, they came across a strange text file on the Desktop.

Credit: Byrch B.

Prompt:

Here is the message: 

b9c52a4e6bd7d06d678fee66ac3066dfe92b43d65fe
1c51004557400a918881e63c4357328e2a804373d10
a668b22299c8c70beec65f7507e7f41a19c5a29153

Flag format: IGE{XXXXXXXX}
```

---

### Soln :

This is also a beginner level challenge.

We are given a hash which is not simple hex. 

I tried using hex decode on CyberChef to ascii but didn't work.

Finally using [crackstation](https://crackstation.net/),

we get our flag : kinghash

#### THE FLAG : IGE{kinghash}

---

Thank you

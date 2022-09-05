from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import random


N = 1
for i in range(25):
	prime = getPrime(random.randint(35, 65))
	N *= prime

e = 65537

msg = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
m = int(msg.encode("UTF-8").hex(), 16)

ct = pow(m, e, N)

print("N:", N)
print("e:", e)
print("ct:", ct)

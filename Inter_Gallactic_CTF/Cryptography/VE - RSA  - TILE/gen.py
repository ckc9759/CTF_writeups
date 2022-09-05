from Crypto.Util.number import *
from Crypto.PublicKey import RSA

p = getPrime(512)
q = getPrime(51)
N = p * q
e = 65537

msg = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
m = int(msg.encode("UTF-8").hex(), 16)

ct = pow(m, e, N)

print("N:", N)
print("e:", e)
print("ct:", ct)

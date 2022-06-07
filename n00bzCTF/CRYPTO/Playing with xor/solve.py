from Crypto.Util.number import *
from pwn import xor

partial_flag = b'n00bz{p'
enc = b"_\x03\x03U\x11\x1e\t]\x07J\x06\x05\x02&F\x02G_4\x1dICl^\x07\x19V&]\x02X\x044\x15\x15\x05J\x02Y\x0c:\x0e\x00G[h\rT\x0b\x02N"
key = b''
flag = b''

for i in range(7):
    key += xor(enc[i], partial_flag[i])

flag = xor(enc, key)

print(flag)
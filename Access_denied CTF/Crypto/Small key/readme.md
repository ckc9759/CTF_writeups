### Chall Desc:
I got the key easily.

### File content:
```py
import os

flag = b"XXXXXX"
key = os.urandom(8)

cipher_text = b""

for i in range(len(flag)):
    cipher_text += bytes([flag[i] ^ key[i % 8]])


print(cipher_text.hex())


# flag 763d32726973a23f79373473616ba86a60300e677634f734482a626f6e5ff22e636a327c2f5ff228240123242e6caa23483d6127765fff6d743a61212f38bb
```

### Soln:

```py
import os

# def calc(flag, ct, key):
#     for i in range(len(flag)):
#         ct += bytes([flag[i] ^ key[i % 8]])
#     return ct

# flag = b"accessdenied"
# temp = b"ac"

# key = os.urandom(8)

# ct = b""
# tmp = b""

# ct = calc(flag, ct, key)
# tmp = calc(temp, tmp, key)

# print(ct.hex())
# print(tmp.hex())

def calc(hex_flag, key):
    flag = ""
    for i in range(len(hex_flag)):
        for j in range(1000):
            if bytes([j ^ key[i%8]]).hex() == hex_flag[i]:
                flag += chr(j)
                break
    return flag

s = b"accessde"
check = ["76", "3d", "32", "72", "69", "73", "a2", "3f"]
newkey = b""
for j in range(len(s)):
    for i in range(1000):
        if bytes([i ^ s[j]]).hex() == check[j]:
            # print(i)
            newkey += bytes([i])
            break

print(len(newkey))

for i in range(len(newkey)):
    print(newkey[i], end=' ')

print()
hex_flag = ["76", "3d", "32", "72", "69", "73", "a2", "3f", "79", "37", "34", "73", "61", "6b", "a8", "6a", "60", "30", "0e", "67", "76", "34", "f7", "34", "48", "2a", "62", "6f", "6e", "5f", "f2", "2e", "63", "6a", "32", "7c", "2f", "5f", "f2", "28", "24", "01", "23", "24", "2e", "6c", "aa", "23", "48", "3d", "61", "27", "76", "5f", "ff", "6d", "74", "3a", "61", "21", "2f", "38", "bb"]

print(calc(hex_flag, newkey))
```

### THE FLAG: `accessdenied{kn0wn_pl41n_t3xt_4tt4ck5_4r3_r34lly_c00l_97cd0658}`

Thank you

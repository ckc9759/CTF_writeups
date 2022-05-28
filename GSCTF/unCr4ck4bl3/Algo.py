#!/usr/bin/env python3
import random

def check_key(key):
    sum=0
    for c in key:
        sum+=ord(c)
    return sum 

key=""
while True:
    key+=random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-_")
    sum = check_key(key)
    if sum>1000:
        key=""
    elif sum==1000:
        print("Password: "+key)
        break

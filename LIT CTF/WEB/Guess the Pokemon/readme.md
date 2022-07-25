### Chall Desc : 
Have you heard the new trending game? GUESS THE POKEMON!!! Please come try out our vast database of pokemons.

#### Soln :

```py
It is a simple SQL injection question. We can try several things to input.
IF we try to input a string under quotation, it says no quotes or backslash.   
It hints towards an sql injection but we are not allowed to use quotation marks.

Therefire,   

1 OR 1=1-- is a simple injection which works in this challenge.
```

#### THE FLAG : LITCTF{flagr3l4t3dt0pok3m0n0rsom3th1ng1dk}

---

Thank you

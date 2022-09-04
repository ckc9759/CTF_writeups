### Chall Desc : Veni, vidi, vici.

---

```py
In adventuring, we often come across many ancient Earthly artifacts 
that we must decipher to be able to sell for the right price. 
Normally, this takes years of experience to master, 
but you might be able to pick up this skill fairly quickly, so take a look!

You turn over the stone tablet handed to you and it reads czkkcv_trvjrij_zj_xffu

Flag format: IGE{XXXXX_XXXXXXX_XX_XXXX}
```

---

### Soln : 

It was a basic beginner challenge. The statement `czkkcv_trvjrij_zj_xffu` seems like a shifted flag.

Veni, vidi, vici is a Latin phrase popularly attributed to Julius Caesar which is mentioned in the challenge name as well.

Therefore, we search for caesar ciphers and then use a decoder to decode the given cipher.

Using [dcode.fr](https://www.dcode.fr/caesar-cipher),

we get the flag : little_caesars_is_good

#### THE FLAG : IGE{little_caesars_is_good}

---

Thank you


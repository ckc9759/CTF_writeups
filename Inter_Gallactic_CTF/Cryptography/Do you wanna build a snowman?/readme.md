### Chall Desc : Do you wanna build a snowman?

```py
Come on let's go and play. I never see you any more. 
Come out the door. It's like you've gone away! We used to be best buddies, 
and now we're not. I wish you would tell me why.

It doesn't have to be a snowman

Flag format: IGE{XXX_XXXXX_XXXXXX_XXX_XXXXX_XXXXXX_XXX_XXXXX}
```

---

### Soln 

```py
──(ckc9759㉿Kali)-[~/Desktop]
└─$ file i_love_snow.txt
i_love_snow.txt: JPEG image data
                                                                                                                                                                                                                                           
┌──(ckc9759㉿Kali)-[~/Desktop]
└─$ stegsnow -C i_love_snow.txt
IGE{how_about_riding_our_bikes_around_the_halls} 
```

#### THE FLAG : IGE{how_about_riding_our_bikes_around_the_halls}

---

Thank you

### Chall Desc : 
I am Esther Man, a brilliant student at Lexington High School. Welcome to my personal website <3 <3 <3

### Soln : 

When we open the website, it seems to be an infinite one and we can never reach the bottom of the page.   
It says click to see the big secret but it's not the flag and just rickroll.

Inspecting the page, we find the first half of flag in the html file itself : 

```
HAHAHAHAHAHAHAHAHAHA I know you will never reach the bottom here because of my infinite scroll. If you somehow did, here is the first third of the half LITCTF{E5th3r_M4
```

The second part was hidden in the style.css file.  

```
.secret {
	/* _i5_s0_OTZ_0TZ_OFZ_4t_ */
	font-size: 50px;

}
```

Combining both the parts gives us the flag.

#### THE FLAG : LITCTF{E5th3r_M4_i5_s0_OTZ_0TZ_OFZ_4t_}

---

Thank you

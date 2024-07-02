### Geoguesser Suite

---

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/97e12899-3000-4dc9-897a-d5cfe098e627)  

This was the second challenge of the `Geoguesser Suite` from UIUCTF 2024.  

Chal.jpg  
  
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/9eae498f-045b-4cb0-959d-4680ee9ca741)  

It seems to be an airport where two planes are visible to us. Directly searching with google lens doesn't reveal anything.

If we zoom in on the grey coloured aircraft, we can observe it's number to be `77182` and the top letters to be `AMC` or something close. The other plane has a human figure printed on it's tail so my first approach was to find these two planes separately.

Searching for the grey coloured plane reveals a lot about it.  
  
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/b227b826-a41b-42da-b464-a784acebdea7)  

The first result is from wikipedia which is also hinted by challenge : `The aircraft name is the same as Wikipedia page title.`  
  
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/49c96f38-5269-42a4-af35-4c5aaa98ca88)  

Hence, we started looking for information on the wiki where we can find the type of plane to be `Boeing C-17A Globemaster III`  

Now, we need to find the location of this aircraft for the coordinates. I goolged for `Boeing C-17A Globemaster III usa airport` which gave many airport locations.
It took us a while to figure out the actual airport, even searching with `AMC` and `77182` didn't help.


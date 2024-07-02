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

Searching for the other plane reveals it's something related to `Alaska Airlines`.
  
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/6dd3525d-7dfa-4914-8bcf-1902e5d53571)

I searched for alaska airlines then and spent quite a while finding the airport. Finally I searched for `alaska airlines boeing c-17 77182` and got this.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/0d0537d8-4405-4b73-9642-2dff053f8726)

It mentions the `Seatac Airport` and the second search also revealed something related to Seattle. To check it's right, I further searched for `seatac airport boeing c-17 77182` and got a youtube video related to this which confirms the surrounding areas as seen from the picture.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/3da7aee5-24cf-4b08-b8a4-e13c04a646b1)

[Youtube](https://www.youtube.com/watch?app=desktop&v=pa2WWaGbzEo)

Matching the correct coords also took a while as the coordinates of seatac airport i.e. `47.4484° N, 122.3086° W` or (`47.449201670709826, -122.30672855323793`) directly don't match even at 3 decimal places.

I tried again the search view and went as close to the runway as possible for the grey plane. 

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/d949d3d8-1d56-434c-8c22-f4ca90187eda)

Got the street view till this point `47.462729349996664, -122.30416232160471` which looked quite close. Using the description `The last digit of the first coordinate is even, and the last digit of the second coordinate is odd.`, I reached finally to the actual answer which was `47.462, -122.303`

Hence, the final flag is

#### Flag : uiuctf{Boeing C-17A Globemaster III, 47.462, -122.303}

---

Thank you  
***ckc9759**



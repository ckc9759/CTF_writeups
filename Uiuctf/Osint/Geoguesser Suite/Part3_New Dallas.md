### Geoguesser Suite

---

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/4b1680e8-b650-43d7-ba40-6a9aaea3176f)

This was the 3rd part of Geoguesser Suite from **UIUCTF 2024**.

Chal.jpg

<img src="https://github.com/ckc9759/CTF_writeups/assets/95117634/d7ceec53-f930-41cd-8fbd-79097d685b13" width="450" height="400">

The given image seems to be taken from a `dashcam` ( Dashboard camera ) and the number plates have been blurred ( geoguesser chall for a reason ).

The description mentions something about trains `Super wide roads with trains... Is this the new Dallas?` so our first thought was to research the train. The top of train looks like a green or cyan coloured strip and it has 6 coaches. We couldn't get much info by searching for the train (Got some results for `Shanghai Metro train line 16` but ignored ) as it was too small to identify any details.

Searching for `dallas` and `new dallas` gave some news articles about the `dallas` city in Texas but it was of no use. Searching for all the train lines running in dallas also didn't give any information regarding our picture.

Zooming the pictue, one can observe the blurred letters which resembles `chinese` or `japanese` characters, thus we shifted our search over there from Texas.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/33734b78-d42b-4a70-b3eb-7e03d1702710)

[Geospy Ai](https://geospy.web.app/) also confirms this thing to some extent, so we start looking for railway lines in China and Japan now ( Still unsure ).

<img src="https://github.com/ckc9759/CTF_writeups/assets/95117634/8cd15c47-cf29-499a-b97b-8ea0d0e130e8" width="850" height="800">

Also, a portion of number plate is visible, a blue number plate with again chinese symbols as it seems, searching for the same almost confirms it's `China`.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/58e619f1-5bf5-484b-9162-8fd90d377386)
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/a58f8bf9-0aa2-434a-8874-15a677283dcd)

I searched for `china railway lines with 6 coaches` and got a huge number of somewhat similiar trains. I had a tough time looking at all the railway lines and was stuck for a while.
I came across list of `high-speed` railway lines on Wiki. I read that but the information available was too overwhelming and pretty hard to locate that train. 

I came across some articles related to `metro` so started working in that direction. It lead to `Shanghai Metro Line` but the images showed a completely different train from what we were looking for. `Shenyang Metro line 10` also looked quite a lot similiar but the colour didn't match (light green).

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/a3c3f20f-fd28-4fc5-a039-468874614c97)

Some of my searches before reaching the actual one :

```txt
Metro lines in China, Green metro lines in China, Green Metro Trains in China,
All green coloured metros in China, Green line metro China, Metro System China,
China railway lines green strip elevated road, High speed green railways China,
China railways with 6 coaches, China Railway Lines, Green trains and many more..
```

I went through the Wiki for all the metro lines in China (Urban rail transit). [LINK](https://en.wikipedia.org/wiki/Urban_rail_transit_in_China)

There were around 50 metro services so I searched all of them 1 by 1 until I searched for `Wuxi Metro line` where the colour and design looked the same `(The colour, the window design and also some pictures with elevated roads)`.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/26b09603-39b3-4e51-8575-524badacf7f6)

I searched the wiki and found that the it was the 2nd line.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/d760c087-21ce-4734-ba3e-67bf1d650782)

After that, it was all gmaps with transit on to find the exact location.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/1cd2e91b-4c69-4d47-9ca9-05032a6cb5ed)
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/ad1942e5-9ae4-4cb4-a6dc-6c602dcceb78)

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/f74255e5-b107-405b-884e-98d3c3cf85b9)

The stretch of Wuxi green line and intersection, guess some digits using the `desc` provided and the chall is solved !

#### Flag : uiuctf{31.579, 120.388} 

Special Mention to `@cha0s` who helped in solving this challenge !

---

Thank you  
***ckc9759***

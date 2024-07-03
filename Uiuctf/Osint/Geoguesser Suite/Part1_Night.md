### Geoguesser Suite

---
<br />

> ## Description:
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/eea7df32-bab8-44d3-8a52-e36fec5f8f40)

This is the first of the three geoguessing challenges in `UIUCTF 2024`.
<br />

> ## Attachments:
Chall.jpg
![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/01e70c25-295c-46c5-b66c-e3e3b1f9dbf2)
<br />

> ## Approach:
The challenge says we need to find the street name and the city from the given image. At first glance, 
we can't figure out anything about the challenge as no text can be found from the image and also it's a night view.

We started searching for the buildings and the background for any clues using Google image search and Yandex. Looking closely, I found that this tower's name or perhaps the logo has been intentionally blurred as hinted from challenge `Some words are blurred out to make the challenge harder, hopefully.`.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/2d59acfe-4c21-48e8-81df-474fa13b899b)

Using google lens, the whole image doesn't return anything useful but some random overbridges and streets.  

Cropping the image portion of the tower and searching for that reveals it is the `Prudential Center` from **Boston** near **Fairmont Copley Plaze**. Searching for this on maps, there's 2 key things you need to notice which is, the position of the adjacent building (`ball like structure on top`) and the type of road which is some kinda underway (goes from below other roads).

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/7b5bba1c-8b59-4a79-980c-67abc5fa93f9)

After this, I started searching with street view of google maps to find the exact location of street from where this photo was taken from.

I tried all the four directions from Prudential Tower to see the orientations. There was some overbridge kind of lines in street views near Prudential tower in the right side so I narrowed down my search over there. 

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/87a00391-904f-4c9e-be06-d6b48da6bcfb)

The right section from prudential tower was an underground road so it wasn't clearly visible. The first similiar picture I could find in street view was on the left side of prudential tower on `I-90` **Massachusetts Turnpike**. `Blue circle` - Prudential Centre, `Red rectangle` - Similarity from the challenge image including the street lights. `I-90` seemed to be correct and now the only task left was to match the background areas to find the street. It took a while using street view to find the location.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/a5084ecb-eb4a-4f3b-af9a-e6e02ff13588)

So next, one can notice there a sign board in original image which allows intersection, that means, the position is around some kind of intersection. Checking all the intersections along the road, we come across the fourth one which is our answer.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/bca85dcc-9712-49c0-a9b0-7b88bc82f981)

Using [Geospy AI](https://geospy.web.app/), we got a similiar result but we needed the street name.

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/c6511f0e-351c-4f7d-929d-0bd8104d4865)

<br />

> ## Final Solve:
Searching on Google earth, ([LINK](https://earth.google.com/web/@42.34795704,-71.06935611,1.89625095a,0d,59.99999999y,251.01081466h,90.06751746t,0r/data=IhoKFkFlWHYxM0hJdE11WmJYUlZjSnNGa2cQAjoDCgEw)), I was able to pin point the location as `157 Arlington Street, Boston, Massachusetts`. The glass building and red building on the left of image for confirming the location

![image](https://github.com/ckc9759/CTF_writeups/assets/95117634/75eb7138-79ec-4175-bf84-f6b2a2d194d2)

Special mention to my teammate `@AkaniX3` who helped a lot in solving this chall.

#### Flag : uiuctf{Arlington Street, Boston}

---

Thank you  
***ckc9759***




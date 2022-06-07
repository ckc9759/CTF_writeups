### Chall Desc:
Some h3ck3rs have been sending secret data using corrupted png's, Find the data!


### File attached:
[corrupt.png](corrupt.png)

#### Soln: 
The file given to us as the name of challenge suggests is corrupted and we are supposed to retrieve it. 
The image isn't opening. 

We use pngcheck to see if it is a png file, it gives us an error.
`chall.png  invalid IHDR image dimensions (0x0)  
ERROR: chall.png`

On using hexedit command we find that the values are different.   
On searching for png image magic number you can find the required hex code and replace the digits as follows:

```py
89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 00 00  .PNG........IHDR....
```
The next 2 sets of 4 pairs of 2 digit hex code define the image width and height which is also tapered in this question.
 
```py
89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 00 00  .PNG........IHDR....
00 00 00 00  08 02 00 00  00 EC 89 1D  43 00 00 00  01 73 52 47  ............C....sRG
```

It is visible that the height and width of image has been set to 0 and 0. we need to increase the dimension to view the image.
```py
89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 05 4D  .PNG........IHDR....
00 00 05 4D  08 02 00 00  00 EC 89 1D  43 00 00 00  01 73 52 47  ............C....sRG
```

The final image:




### THE FLAG: n00bz{h0w_7he_h41l_d1d_y0u_f1x_th1s?!!}

Thank you

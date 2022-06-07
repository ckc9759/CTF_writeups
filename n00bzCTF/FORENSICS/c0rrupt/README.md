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

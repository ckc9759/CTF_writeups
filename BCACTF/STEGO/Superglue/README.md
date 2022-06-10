### Chall Desc:
I accidentally glued my images together. Please help!

### File attached:
[chall](C)

### Soln:

We are given a file which does not open.  
It is because there are actually four images concatenated into one file.   
Opening in a hex editor and changing their magic numbers reveals the flag in parts.

```js
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ file C
C: JPEG image data, JFIF standard 1.01, resolution (DPI), density 300x300, segment length 16, baseline, precision 8, 27x5, components 3
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ pngcheck C
C  this is neither a PNG or JNG image nor a MNG stream
ERROR: C
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ binwalk C

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
441           0x1B9           PNG image, 27 x 5, 8-bit/color RGB, non-interlaced
980           0x3D4           GIF image data, version "89a", 27 x 5
```

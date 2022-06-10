### Chall Desc:
My friend said that he made a really cool drawing in MS Paint but I can't open it! Maybe my computer is broken?   
Or the image? I really don't know. Could you try opening it for me and telling me what it is?

### File attached: [chall.svg](chall.svg)

### Soln:

The image is a svg file which doesn't open. 
Hence we look for file details using FILE command and we find that it is a png file.

Therefore, we change the extension of file.

```python
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ file chall.svg
chall.svg: PNG image data, 1011 x 169, 8-bit/color RGB, non-interlaced
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ hexedit chall.svg

[6]+  Stopped                 hexedit chall.svg
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ mv chall.svg chall.png
 ```
 
Hex (using Hexedit command) of file:  
 
```python
00000000   89 50 4E 47  0D 0A 1A 0A  00 00 00 0D  49 48 44 52  00 00 03 F3  .PNG........IHDR....
00000014   00 00 00 A9  08 02 00 00  00 E8 63 FA  F8 00 00 00  01 73 52 47  ..........c......sRG
00000028   42 00 AE CE  1C E9 00 00  00 04 67 41  4D 41 00 00  B1 8F 0B FC  B.........gAMA......
```

On changing the file extension it opens,
![](chall.png)

Thank you

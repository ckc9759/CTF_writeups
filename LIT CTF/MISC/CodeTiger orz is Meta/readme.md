### Chall Desc : 
can you find the flag from this amazing codetiger fan picture!!

### File attached : 
![codetigerfanpic.png](codetigerfanpic.png)

### Soln : 

We are hinted with the chal description that the data is inside the metadata of the png file.  
We use foremost and exiftool and we can see the parts of the flag. Joining them generates the flag for us.

```py
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ exiftool codetigerfanpic.png
ExifTool Version Number         : 11.88
File Name                       : codetigerfanpic.png
Directory                       : .
File Size                       : 27 kB
File Modification Date/Time     : 2022:07:23 09:25:51+05:30
File Access Date/Time           : 2022:07:25 17:00:06+05:30
File Inode Change Date/Time     : 2022:07:25 16:58:04+05:30
File Permissions                : rwxrwxrwx
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1536
Image Height                    : 864
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Gamma                           : 2.2
Pixels Per Unit X               : 4724
Pixels Per Unit Y               : 4724
Pixel Units                     : meters
Coded Character Set             : UTF8
Envelope Record Version         : 4
Object Name                     : LITCTF{c0de_
Copyright Notice                : orz}
Caption-Abstract                : t1g2r_
Application Record Version      : 4
XMP Toolkit                     : Image::ExifTool 12.36
Description                     : t1g2r_
Rights                          : orz}
Title                           : LITCTF{c0de_
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : t1g2r_
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Copyright                       : orz}
Image Size                      : 1536x864
Megapixels                      : 1.3
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ strings codetigerfanpic.png | grep "LITCTF"
    <rdf:li xml:lang='x-default'>LITCTF{c0de_</rdf:li>
```

#### THE FLAG : LITCTF{c0de_t1g2r_orz}

---

Thank you

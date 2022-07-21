### Chall Desc : 

I'm stuck in the Dark.

Attachments

![fireflies.gif](fireflies.gif)

### Soln : 

In this challenge, we are given a gif file. On opening the gif, we don't see anything relevant.
The chall name suggests we need to analyze the file.

I used strings with grep command to see if there is any flag hidden there. Then i tried exiftool and foremost.

Finally on using binwalk, we can see there is a .rar file hidden inside.

```cpp
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ file fireflies.gif
fireflies.gif: GIF image data, version 89a, 268 x 340
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ strings fireflies.gif | grep "BDSEC"
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ strings fireflies.gif | grep "sec{"
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ strings fireflies.gif | grep "c{"
JVD1c{
Tjc{
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ exiftool fireflies.gif
ExifTool Version Number         : 11.88
File Name                       : fireflies.gif
Directory                       : .
File Size                       : 1035 kB
File Modification Date/Time     : 2022:07:21 13:08:39+05:30
File Access Date/Time           : 2022:07:21 13:16:45+05:30
File Inode Change Date/Time     : 2022:07:21 13:08:39+05:30
File Permissions                : rwxrwxrwx
File Type                       : GIF
File Type Extension             : gif
MIME Type                       : image/gif
GIF Version                     : 89a
Image Width                     : 268
Image Height                    : 340
Has Color Map                   : Yes
Color Resolution Depth          : 8
Bits Per Pixel                  : 8
Background Color                : 251
Animation Iterations            : Infinite
Frame Count                     : 32
Duration                        : 2.88 s
Image Size                      : 268x340
Megapixels                      : 0.091
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ binwalk fireflies.gif

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             GIF image data, version "89a", 268 x 340
154302        0x25ABE         PARity archive data
1059353       0x102A19        RAR archive data, version 5.x

ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$
```

On using `binwalk -e fireflies.gif` , we get the rar file which contains a file named cry100.

Contents of the file :

```py
Sld xlfow R yv hl olhg
Rm z kozxv R pmld hl dvoo?
Sld xlfow R yv hl yilpvm
Rm z uznrob hl gltvgsvi?
Sld xlfow R yv hl olmvob
Hfiilfmwvw yb hl nzmb?
Sld xlfow R yv hl fmszkkb
Hfiilfmwvw yb hl nfxs yvzfgb?
Sld xlfow R yv nv
Dsvm vevm R ivnzrm z nbhgvib?
YWHVX{N33n_gsv_yfggviuob_tlvh_fk_fk_zmw_zdzb}
```

Using cipher identifier on dcode.fr, we know that this is `Atbash cipher`.

Decoding the flag we get,

#### THE FLAG : BDSEC{M33m_the_butterfly_goes_up_up_and_away}

---

Thank you

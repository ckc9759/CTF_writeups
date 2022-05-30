### Chal Desc:  
I found this flag on the CTF admin's computer, so I figured I'd just give it to you. The only problem is that it's not opening for me...

### File attached: flag.png

Soln: On opening the file, we find it doesn't open. Using file command, we know it is ASCII text.
Opening hex editor using HEXEDIT command in bash, we get a string ""

```hex
00000000   23 20 54 68  69 73 20 66  69 6C 65 20  75 73 65 73  20 63 65 6E  # This file uses cen
00000014   74 69 6D 65  74 65 72 73  20 61 73 20  75 6E 69 74  73 20 66 6F  timeters as units fo
00000028   72 20 6E 6F  6E 2D 70 61  72 61 6D 65  74 72 69 63  20 63 6F 6F  r non-parametric coo
0000003C   72 64 69 6E  61 74 65 73  2E 0A 0A 6D  74 6C 6C 69  62 20 62 79  rdinates...mtllib by
00000050   75 32 2E 6D  74 6C 0A 67  20 64 65 66  61 75 6C 74  0A 76 20 35  u2.mtl.g default.v 5
```

Searching this string on Google, we find that it is an obj file and the files has coordinates of 3d that can be opened using any 3d software such as Blender or in any online website.

Using Wireframe view, we get the flag embedded inside the object.

Thank you
[Ckc9759](https://github.com/ckc1404)

### Chal Desc:
The local Konica Minolta printer overheated. Can you find out why?

### File attached: 
[corrupt.lava](corrupt.lava)

#### Soln:
 
It required some thinking.  
Firstly when i tried few commands on the lava file, nothing substantial i could find.
I got this:

```py
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ file corrupt.lava
corrupt.lava: HP Printer Job Language data
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ strings corrupt.lava
%-12345X@PJL JOB NAME="wrap in 'n00bz{}'"
%-12345X@PJL JOB USERNAME="0xBlue"
%-12345X@PJL JOB TIMESTAMP="05/31/2022"
%-12345X@PJL JOB OSINFO="Blue0S"
%-12345X@PJL ENTER LANGUAGE=LAVAFLOW
&l0S
&l0G
&u146D
&l154X
.
.
.
&l0H
%-12345X
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$
```

This info was useless. Then i tried:

```python
ckc9759@ckc:/mnt/c/Users/Chaitanya K Chauhan/downloads$ cat corrupt.lava
2345X@PJL JOB NAME="wrap in 'n00bz{}'"
2345X@PJL JOB USERNAME="0xBlue"
2345X@PJL JOB TIMESTAMP="05/31/2022"
2345X@PJL JOB OSINFO="Blue0S"
2345X@PJL ENTER LANGUAGE=LAVAFLOW

0S0G146D154X157X0O157U162W�X151M1A3H1M163E154S141T0U0Z166X141Y1A20VPl�\3W��l�6��q%H��|6��٠�-��@�8�8�8�8�8�8�8�8�8�8�8�8�Ϳ��8�^~Z��PǦ���,��F%���qIo�2        �;����������������������@%@@��
                                                                                                       �$�oҤ��/Gx��8a|����J��I$�I$�I$�I$�I$�I$�I$�I$�I$�I$�lp.!\�.+r~���""��~�
                                                                             ��E6���z�EQEQEQEQEQEQEQEQEQE��$k��4�
```

It started making some sense. There were few characters and then a set of 3 numbers.
I collected those numbers and tried different ways to decode it.
1. Firstly i found their hex and then using ascii decoding but that was wrong.  
https://www.dcode.fr/ascii-code
2. Then i converted the decimal to binary and then binary decoder but it was not a UTF-8 encoded text.  
https://cryptii.com/pipes/binary-decoder
3. Then i converted them to octal and used cyberchef to get the line required: "FLOORISLAVA" . (my team member helped me decoding it)
https://gchq.github.io/CyberChef/#recipe=Magic(3,false,false,'')

```abc
146 154 157 157 162 151 163 154 141 166 141  --- DECIMAL

92 9A 9D 9D A2 97 A3 9A 8D A6 8D  --- HEXADECIMAL

10010010 10011010 10011101 10011101 10100010 10010111 10100011 10011010 10001101 10100110 10001101  --- BINARY

222 232 235 235 242 227 243 232 215 246 215   --- OCTAL
```
<h>
 <img src="https://user-images.githubusercontent.com/95117634/172211383-1d566f11-3251-4ec8-8932-8f2b89bd8324.png" width="800" height="400">
</h>

#### THE FLAG: n00bz{floorislava}

Thank you


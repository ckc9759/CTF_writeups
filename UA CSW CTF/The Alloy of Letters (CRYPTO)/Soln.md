### Chall Desc:
In the three hundred years since the events of me writing this down, science and technology have marched on.

#### file Desc: 
[file.txt](https://github.com/ckc1404/CTF_writeups/files/8826263/flag.txt)

#### Soln:  

Punch it into https://www.dcode.fr/cipher-identifier and notice that it very positively recognizes it as ASCII shift.  

The top brute force hit looks a lot like natural language with the spacing, casing and all printable ASCII.

Feed as much text as you can fit into Guballa's eminent substitution cipher solver: https://www.guballa.de/substitution-solver with the English setting.  

The flag should be easily decipherable from the result.

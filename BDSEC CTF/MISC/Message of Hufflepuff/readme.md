### Chall Desc : 

One day, Harry Potter was roaming around the Hufflepuff, one of the four Hogwarts houses. 
Inside one of the room of Hufflepuff, he found a secret numeric message and a graph. 
Now, he is curious to know what is written in the secret neumeric message. Can you help him to figure it out?

### File attached : 

[Message_of_Hufflepuff.png](Message_of_Hufflepuff.png)  
[msg.txt](K.txt)

### Soln :

Looking at the picture, it appeared to be a binary tree. I searched for sometimes, and found an image which said huffman coding when i searched for tree cipher ctfs.
The challenge name also suggested something related to hufflepuff.

Now, when i read about huffman encoding algorithm, i got to know it is based on frequency. We are given a binary string in msg.txt, the binary strings are basically the characters they are pointing to.

In a binary tree, every left child can be denoted by a 0 and a right child with a 1. So, i manually found each character and concatenated it to get the flag. We can also run a script for the same.

converted msg.txt

```cpp
00101  --> B
111    --> D
00110  --> S
1011   --> E
1001   --> C
00111  --> { and so on
00010      .
01000      .
1000
1000
00100
01011
1101
1100
1011
1101
00001
01100
01001
01101
1101
1010
1100
1010
01010
01110
1100
111
01111
1001
00011
111
01111
111
00000
```


#### THE FLAG : BDSEC{Huffm@n_Enc0d1ng_go7_D3COD3D}

---

Thank you

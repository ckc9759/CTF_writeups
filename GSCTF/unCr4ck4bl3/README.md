Playlist to learn binary exploitation

https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN

Challenge is based on binary exploitation.
We have to disassemble the main function (which can be done by any disassembler like gdb or radare2 ) 
and look for the 'if' condition which checks for the password. And the password is nothing but the string in which the sum of ascii code of characters is 1000.

The loop which calculates sum can be easily spotted. So entering any string whose char sum is 1000 will give you the flag.

Algorithm in the question is a python script which generates a random string whose sum is 1000.

The challenge also contains a false flag (GSCTF{4r3_y0u_5ur3_4b0ut_th4t7}) which can be obtained by some basic commands like strings.

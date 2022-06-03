#### Chal Desc: 


### file attached: 


### Soln:  

Extract the Normal_Picture_Stuff.zip zip from the Pandora image:  

```cmd
 steghide extract -sf Pandora.jpg -p password
```  

Do a dictionary attack on the zip (password: imagenius). Unzip the zip, getting another Image_Data.zip zip and a Passwords.txt file.


In the Passwords.txt file, pass the first line from a base64 decoder, 
and the second line from a base32 decoder, followed by base 64, ending up with two strings in binary base. 
Xor the two getting the password: PlE4sE_L3t_ME_IN.  

Decompress the Image_Data zip getting a dude.jpg image. Change the visible size of the image finding the flag:

This can be done with CyberChef,   
following the procedure in this link: https://blog.cyberhacktics.com/hiding-information-by-changing-an-images-height/

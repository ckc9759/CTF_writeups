# Soln for Chad_the_jaw challenge...

## DESC: 
Chad "The Jaw" likes nothing more than pumping iron and looking good.  
He left behind a favorite song of his for us to analyze.  
Can you find his deepest, darkest secret?

### HINT:
This multi-step challenge combines steg, OSINT, ciphers, and password cracking all into one amazing Chad-y challenge!  

#### On hearing the mp3 file, you will find an abrubt ending in the end..  
Using Sonic Visualizer or any spectrogram adding tool, you can find a code in the image..  

![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170844536-23f69f75-fdfc-4b7f-8601-6c190f0cdf3c.png)

After searching on twitter for chad, i found a profile named as Giga Chad:  https://twitter.com/ChadTheJaw    
![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170845800-8ed4ebbe-5cf8-405a-8c2f-653e8f0442fb.png)  


On the twitter page, you can find a suspicious page saying look at me now:  
![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170844566-fb8d40d2-780d-413e-9f3e-922996528230.png)    

![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170845774-961dadae-2d5b-4834-866f-35d9d67c8d0b.png)  

Upon downloadling this file I noticed that it was unusually large 16MB for a small jpg,  
I loaded it into a hex editor and it looked like there was other content hidden in that image,  
eventually I found that there was a rar file inside:  

![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170844653-d58d7051-7889-47b7-b8bc-c99652b27285.png)  
I cleaned up the file removing the png section that was before the "Rar!" I was left with an password locked rar file:  

Not knowing the password to unlock these files I poked around on the twitter again and found this text file.Using this I was able to decypt this by counting the ammount of "chads" and "thejaws" the corelated the number to letters in the alphabet you can see my thought process here:  

![ckc](https://github.com/ckc1404/CTF_writeups/blob/main/BYU%20CTF/Chad_the_jaw/170875008-af66fe05-f0d0-4524-b7d9-c682d06ac6d9.png)  

You can find the Flag in 
### left bottom corner...

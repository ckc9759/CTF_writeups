# Soln for Chad_the_jaw challenge...

## DESC: 
Chad "The Jaw" likes nothing more than pumping iron and looking good.  
He left behind a favorite song of his for us to analyze.  
Can you find his deepest, darkest secret?

### HINT:
This multi-step challenge combines steg, OSINT, ciphers, and password cracking all into one amazing Chad-y challenge!  

#### On hearing the mp3 file, you will find an abrubt ending in the end..  
Using Sonic Visualizer or any spectrogram adding tool, you can find a code in the image..  

![ckc](https://user-images.githubusercontent.com/95117634/171095017-76022fbd-e39f-4e65-9e86-32c9dd895bf5.png)

After searching on twitter for chad, i found a profile named as Giga Chad:  https://twitter.com/ChadTheJaw    
![ckc](https://user-images.githubusercontent.com/95117634/171094920-11f9d79c-3ed9-4430-a1db-89397475776c.png)  


On the twitter page, you can find a suspicious page saying look at me now:  
![ckc](https://user-images.githubusercontent.com/95117634/171095067-60e17a1a-609a-49ec-83cc-527d522a7370.png)    

![ckc](https://user-images.githubusercontent.com/95117634/171094843-c5b273e3-2da3-44f6-a35a-886378547781.png)  

Upon downloadling this file I noticed that it was unusually large 16MB for a small jpg,  
I loaded it into a hex editor and it looked like there was other content hidden in that image,  
eventually I found that there was a rar file inside:  

![ckc](https://user-images.githubusercontent.com/95117634/171094782-408a14c3-0606-4cf7-8910-bffc0b30abf2.png)  
I cleaned up the file removing the png section that was before the "Rar!" I was left with an password locked rar file:  

Not knowing the password to unlock these files I poked around on the twitter again and found this text file.Using this I was able to decypt this by counting the ammount of "chads" and "thejaws" the corelated the number to letters in the alphabet you can see my thought process here:  

![ckc](https://user-images.githubusercontent.com/95117634/171094526-bc7e98db-2db4-4d4d-a013-a48ae1f10fe9.png)  

You can find the Flag in 
### left bottom corner...

Thank you  
[Ckc9759](https://github.com/ckc1404)

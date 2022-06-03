### Chal Desc:


#### File attached: 


#### Soln: 

Download the Duck.png for the challenge. Use strings in de Duck.png, where you can see the string in Base64 
```a
 nUE0pUZ6Yl93q3phoJIxnJSznKWyYzAioF9znJkyY3E3AwHjoGM6BGW1oGDjpP9RqJAerF5dpTpiMzyfMD== 
```

Decode from Base64 and get the mediafire link 
 https://www.mediafire.com/file/tw650m6z92um40p/Ducky.jpg/file .
 
 Then use the text in the image you got (DON'T DUCK WITH ME) as a passphrase in steghide with the Ducky.jpg, something like this should do 
 ```bash
 steghide extract -sf Ducky.jpg -p "DON'T DUCK WITH ME" 
 ```
 
 You can use other tools, tho . 
 With this you get a zip named Gooooooose.zip, now you can extract it, and get a image named Gooooooose.jpeg, then just use the strings with the grep command to get the flag. 
 Like this 
 ```ubuntu
 strings Gooooooose.jpeg | grep 'CTF.*' 
 ```

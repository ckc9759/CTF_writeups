### Chal Desc:
I just mixed all my challenges together, enjoy.

### File attached: 


### Soln: Start by downloading the 2 images provided by the challenge.  

With GenasiDndSize.jpg change the visible size of the image to see the password  pLE4sE_L3t_ME_iN_1 ,
you can do it by change the bytes of the images that define it's height.   

Link of related blog: https://blog.cyberhacktics.com/hiding-information-by-changing-an-images-height/  

Use the password found as passphrase in steghide with GenasiSteg.jpg.

Then in the file extrated named My_File_Is_To_BigSorry:(.txt, you get the link to the next image named GenasiBoy.png. 
```python
If you use strings in this images you will get a base64 string.  

If you decode it with base64 and url decoder you will get a link to a twitter acount.  
```

This twitter acount has one tweet with a image, and in the tweet there are a link to get the image named SuperGenasi.png.
```python
For last you can XOR the GenasiBoy.png and SuperGenasi.png getting a image that looks like a girl,
then you can see the the red plane 3 of the image and get the flag.   
```

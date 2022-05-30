### Chall Desc: 
To prevent the need to brute force submit what may seem to be multiple likely answers, I have provided the MD5 hash of the entire flag so you can verify that you have it right before submitting it online (lessening load on the server).

63b1424fa6fe8aa81d9ce4b5637f7acd

### File attached: [reconstruct.png](https://user-images.githubusercontent.com/95117634/171031262-2380a927-5d56-4c66-a788-f41bce0cec52.png)

Soln:  
On viewing the file, we find that the flag is given right away but it has been hidden with a black line that is not removable with image edittors or LSB shift.

Hence, we try to decipher the letters using intution and examining the given strings visible parts
![ckc](https://user-images.githubusercontent.com/95117634/171031262-2380a927-5d56-4c66-a788-f41bce0cec52.png)

If we look closely, we can identify letters and numbers such as l with it's curve, 1, h with it's shape having two curved bottoms.  
Then we also observe a is visible using it's characteristic bottom shape 'a'.
Letter f is also evident. 'n' also becomes visible with zooming.

Hence with just intution we can get a part of the flag i.e **{...n_.1th_th._l1ttl..t_.f_1nf._1_.an_....n.t...t_1t}**

We can make the flag after that, just that long string remains where the Chall name reconstruct just fits perfectly and BOOM !! we solved the challenge.

Flag: {even_w1th_the_l1ttlest_of_1nfo_1_can_.reconstruct_1t}
Verifying the flag with the md5 hash, we can submit the flag.

Thank you  
[Ckc9759](https://github.com/ckc1404)


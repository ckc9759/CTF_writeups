### Chall Desc:
John Doe is on the run!   
Find the city in which he's planning to meet someone! Start your journey by the social media ccount name noobpeople9999.   
Example flag: n00bz{new_york}

### File attached: none

#### Soln: (Author ckc9759 Amol_agg)

We are given a username `noonbpeople9999`. On searching it on Google, a facebook account comes up with that username but that is irrelevant.
Then, there was an instagram account with that username.

![inst](https://user-images.githubusercontent.com/95117634/172290261-ecc2bd10-fb4a-48cc-adbd-ef34ab2435ae.png)

If you observe, there are some letters in bold while rest are not. That looks weird.
After searching for a while, i found it is some kind of twitter cipher. On searching "twitter stego" we get the decoder site:  
https://holloway.nz/steg/

![tweet](https://user-images.githubusercontent.com/95117634/172291067-8770dd18-7c19-4aa9-8f8c-88a1089d6f88.png)

It gives us another username and this time, it is a twitter username: `noobmas55827604`

![jj](https://user-images.githubusercontent.com/95117634/172292376-cfa2d90d-0d0f-40d3-a925-639cf9175b01.png)

There is a link, which gives us a pcapng file. On loading it in `wireshark` and following the tcp stream, we get a link: https://s1.fdow.nl/u6QfK-chall.jpg
that gives us an image.

![](https://user-images.githubusercontent.com/95117634/172292655-80cebeb1-b9df-46f1-a916-167d2f20adf7.jpg)

Using reverse search tools, i went on to find a similiar image for about 12-13 hours. I searched it on Google, yahoo, flickr, tinyimage, bing and many others.  

Finally i found this on `yandex` which was the right answer. In the top right corner, you can see the location is mentioned

![](https://user-images.githubusercontent.com/95117634/172292767-dc48165b-9787-4cc5-8241-a493445e88d2.png)

#### THE FLAG: n00bz{new_kakhovka_plavni}

Thank you

### Chall Desc:
Our agents managed to capture some https traffic of our target, can you decrypt it and find out where he's planning to go?
Flag format n00bz{city_name_in_lowercase}

### File attached: 


#### Soln: (Author FusterCluck)
We are given a pcapng file along with https keys used for decrypting https traffic. We decrypt the traffic using wireshark (img1) and analyze the https data.

To find the city he went to, we look throught the http2 data to find a packet leading to a wikipedia page referencing Kapellbrücke (img2). We visit the page to see that its located in a city called Lucerne.

`Flag: n00bz{lucerne}`

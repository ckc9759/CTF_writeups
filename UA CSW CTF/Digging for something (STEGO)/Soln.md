### Chal Desc:
Someone was Digging Near Santa Maria da Feira, can you find what?

### File attached: [capture.pcapng]()

#### Soln: 

Filter the queries by DNS.  
![](https://user-images.githubusercontent.com/95117634/171793708-a809ad57-2688-4541-abb4-6a389b92a478.png)

tshark to extract all DNS queries from 192.168.122.143

tshark -r capture.pcapng -T fields -e dns.qry.name ip.src == 192.168.122.143  

![](https://user-images.githubusercontent.com/95117634/171793837-db4172d7-09bb-4443-9619-fc5339dc2b57.png)

Cleaning up duplicates and joining them together, before base64 decoding

![](https://user-images.githubusercontent.com/95117634/171793951-27b7be68-d622-45be-b709-ef2c30944842.png)

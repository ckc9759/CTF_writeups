### Chal Desc:
Someone was Digging Near Santa Maria da Feira, can you find what?

### File attached: [capture.pcapng]()

#### Soln: 

Filter the queries by DNS.  


tshark to extract all DNS queries from 192.168.122.143

tshark -r capture.pcapng -T fields -e dns.qry.name ip.src == 192.168.122.143  



Cleaning up duplicates and joining them together, before base64 decoding

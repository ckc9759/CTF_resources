### N o T e S

---

Packets can be thought of as self contained units that contain information being sent by computers(amongst other things). The network layer uses the Internet Protocol(IP) to ensure that packets reach the correct destination. These packets use the source and destination IPs to ensure that they reach the correct destination.


#### ( TCP - Transmission Control Protocol )

```py
TCP is a connection oriented, reliable transmission protocol. 

- TCP uses acknowledgement to ensure that data is retransmitted even if it is dropped.
- TCP uses sequence numbers to keep track of the order in which data is being sent. 
- TCP uses mechanisms to ensure that there’s no congestion when data is being transmitted.
```

#### Scanning TCP : 

```py
You can use nmap to scan for TCP services:

nmap -sT -p port-number -O -sC -sV -T[1-5] -oA output-file-name ip-address
```

#### ( UDP - User Datagram Protocol )

```py
This protocol is a connectionless, stateless protocol. Unlike TCP, it doesn’t focus on reliability or creating a connection. 
This is useful in scenarios where the loss of data is tolerated e.g. streaming video and audio. 
```

#### UDP Scanning : 

```py
UDP Scanning

UDP scanning uses the same combination as above. Instead of using the -sT or -sS scan type, it uses the -sU flag to specify a UDP scan. 
```




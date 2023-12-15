## What to do with a pcap file ???

---

[wireshark](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/wireshark-tricks)

- Look for it's tcp stream, if you find something change it to raw and then save it. Maybe, there is another file or something hidden there.

- Sometimes, there is a PNG file inside pcapng which is transmitted through a particular traffic like ICMP or TCP etc. In such cases you need to find all the matching packets and ending packet and then combine those packets using `tshark` and then use any hex editor for writing those hex down and then saving the png image.
- When asked for passwords, search in the `https` protocols.

- ssf
- command - `strings f4.pcapng | grep -i "GET /"`

- In pcapng file, we can use view to search for strings using search packet option.
- The `Black` segments in the pcap packets denote that the data has been segmented into different packets.
- We can export all the objects of HTTP packets and try to assemble them.
- If we found any RSA private key, use it to decrypt using ssl protocol inside the preferences and using user IP from the pcap file.

---


### Data Exfiltration

```py
It is the technique of of transferring unathorized data out of the network.
Data exfiltration techniques : 

- DNS
- FTP/SFTP based file transfer
- SMB based file transfer
- HTTP/HTTPS 
- Steganographical methods, like hiding data within images
- ICMP
- And many more. The sky's the limit for Exfiltration methods.
```

- Some attackers may attempt to obfuscate the data further by placing the data in an encrypted zip file.

---

### Cracking zip files : 

```py
fcrackzip -b --method 2 -D -p /usr/share/wordlists/rockyou.txt -v ./file.zip
```

### Exporting files from tcp or http or any other stream : 

```py
file then export objects and then choose the stream and save them all.
```








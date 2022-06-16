### What to do with a pcap file ???

- Look for it's tcp stream, if you find something change it to raw and then save it. Maybe, there is another file or something hidden there.

- Sometimes, there is a PNG file inside pcapng which is transmitted through a particular traffic like ICMP or TCP etc. In such cases you need to find all the matching packets and ending packet and then combine those packets using `tshark` and then use any hex editor for writing those hex down and then saving the png image.

- ssf
- command - `strings f4.pcapng | grep -i "GET /"`

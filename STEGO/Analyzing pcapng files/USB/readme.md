### Universal Serial Bus

---

```php
tshark -r tdk_challenge.pcap -Y usb.capdata -T fields -e usb.capdata > raw

xxd -r -p raw raw.bin

binwalk --dd='.*' raw.bin 
```

We cannot follow tcp or udb streams. 

`URB_INTERRUP` --> Keyboard, keystrokes.

Filter

#### Use the commands on filtered packets saved as a new file
```php
usb.transfer_type==0x01 and frame.len==35 and !(usb.capdata==00:00:00:00:00:00:00:00)
tshark -r example.pcap -T fields -e usb.capdata > usbdata.txt
```
```php
tshark -r ./Flag_Filter.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystroke.txt
tshark -r ./keyboard.pcapng -Y 'usbhid.data' -T fields -e usbhid.data > keydata.txt
```

1. [USB WIKI](https://github.com/mahaloz/ctf-wiki-en/blob/master/docs/misc/traffic/protocols/USB.md)
2. [usb](https://ctf-wiki.mahaloz.re/misc/traffic/protocols/USB/)  
3. [kaizenctf](https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4)  
4. [wireshark](https://wiki.wireshark.org/USB)  
5. [nutshell](https://www.beyondlogic.org/usbnutshell/usb4.shtml#Interrupt)  
6. [hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/usb-keystrokes)
7. [vishwa](https://github.com/CBC-MIT/CTF-Writeups/blob/main/VishwaCTF2k23/1nj3ct0r/README.md)
8. [HID](https://medium.com/@sidharthpanda1/usb-sniffer-packet-challenge-cryptoverse-ctf-forensics-c42f2975e8f1)
9. [Mouse,HID](https://res260.medium.com/usb-pcap-forensics-graphics-tablet-nsec-ctf-2021-writeup-part-2-3-9c6265ca4c40)
10. [ACSC](https://seriotonctf.github.io/2023/02/26/pcap-1-Writeup-ACSC-2023/index.html)
11. [URB BULK_BITS](https://blogs.tunelko.com/2017/02/05/bitsctf-tom-and-jerry-50-points/)
12. 

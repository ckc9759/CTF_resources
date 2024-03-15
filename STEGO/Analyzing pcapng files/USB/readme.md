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
```

[usb](https://ctf-wiki.mahaloz.re/misc/traffic/protocols/USB/)  
[kaizenctf](https://abawazeeer.medium.com/kaizen-ctf-2018-reverse-engineer-usb-keystrok-from-pcap-file-2412351679f4)  
[wireshark](https://wiki.wireshark.org/USB)  
[nutshell](https://www.beyondlogic.org/usbnutshell/usb4.shtml#Interrupt)  
[hacktricks](https://book.hacktricks.xyz/generic-methodologies-and-resources/basic-forensic-methodology/pcap-inspection/usb-keystrokes)

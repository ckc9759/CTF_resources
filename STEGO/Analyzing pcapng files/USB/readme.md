### Universal Serial Bus

---

```php
tshark -r tdk_challenge.pcap -Y usb.capdata -T field -e usb.capdata > raw

xxd -r -p raw raw.bin

binwalk --dd='.*' raw.bin 
```

We cannot follow tcp or udb streams. 

`URB_INTERRUP` --> Keyboard, keystrokes.

Filter
```php
usb.transfer_type==0x01 and frame.len==35 and !(usb.capdata==00:00:00:00:00:00:00:00)
```
```php
tshark -r ./Flag_Filter.pcap -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystroke.txt
```

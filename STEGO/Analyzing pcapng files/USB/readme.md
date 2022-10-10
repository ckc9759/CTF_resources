### Universal Serial Bus

---

```php
tshark -r tdk_challenge.pcap -Y usb.capdata -T field -e usb.capdata > raw

xxd -r -p raw raw.bin

binwalk --dd='.*' raw.bin 
```



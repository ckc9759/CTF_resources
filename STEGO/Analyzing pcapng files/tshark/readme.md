### tshark

---

```py
$ tshark -r chall.pcap -Y 'frame.number gt 4 && tcp.payload' -Tfields -e tcp.payload
| xargs -n2 | awk '{print substr($2,1,2)$1}' | paste -sd '' | cut -c113- | xxd -r -p > flag.jpg4
```

```py
tshark -r traffic_capture.pcapng -Y "icmp.type==8"  -Tfields -e data.data  > new.txt
```

```py
tshark -r capture.pcapng -Y "frame.len==71" -T fields -e "usbhid.data.axis.x" -e "usbhid.data.axis.y" > a.txt
-r for reading the capture.
-Y for filter used.
-T to set the fields flag.
-e for extracting the required info needed, in this case (usbhid.data.axis.x) && (usbhid.data.axis.y).
```

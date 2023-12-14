### NOTES

---

```py
tshark -r dnscap.pcap -Tfields -e dns.qry.name > names.txt

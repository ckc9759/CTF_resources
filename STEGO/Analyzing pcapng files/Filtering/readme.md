### Filtering

---

```py
ip contains key --> It searches for all the packets that have "key" related things in them. It could be a file .zip .txt anything
```

```py
tcp contains "backup" -> searches for tcp stream which have backup transfer going on or all the packet transfers having backup string in it.
```

---

`SYN attack is a common attack used and commonly found in pcap transfer files`

Analyze the tcp streams using the analyze section.

```py
Search for protocol hierarchy and export objects accordingly 
Maybe data is hidden in FTP protocol or some other protocol.
Everytime, we don't use TCP and HTTP for transmitting data.
```

#### Filtering by length and protocol

```py
data.len == 41 and UDP
```


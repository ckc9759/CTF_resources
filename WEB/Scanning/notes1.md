### Notes :

---

#### looking at txt record of a web server.

```py
nslookup -q=txt key.z.hackycorp.com
Server:         172.24.2.76
Address:        172.24.2.76#53

Non-authoritative answer:
key.z.hackycorp.com     text = "9f883f22-6ea5-4631-bbe8-95841ad63f56"

Authoritative answers can be found from:

```

---


#### DNS Transport Zone vulnerability

```py
dig @z.hackycorp.com z.hackycorp.com axfr
```

---

```py
dig @z.hackycorp.com "int" axfr
```

---

#### Bind version

```py
dig@abc.com version.bind chaos txt
```

---


                                                                                                                                                                                                                            

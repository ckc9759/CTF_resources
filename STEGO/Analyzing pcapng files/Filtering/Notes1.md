```c
Wireshark filters for analyst

1. Filter by IP address:
“ip.addr == x.x.x.x", where "x.x.x.x" is the IP address you want to filter

2. Filter by IP address range:
"ip.addr >= x.x.x.x and ip.addr <= y.y.y.y", where "x.x.x.x" and "y.y.y.y" are the start and end IP addresses of the range

3. Filter by network interface:
"interface == eth0" to show only packets captured on the eth0 interface

4. Filter by port:
"tcp.port == 80" or "udp.port == 53", where "80" and "53" are the port numbers you want to filter

5. Filter by packet length:
"frame.len > 100" to show only packets that are longer than 100 bytes

6. Filter by source or destination MAC address:
"eth.src == xx:xx:xx:xx:xx:xx" or "eth.dst == xx:xx:xx:xx:xx:xx", where "xx:xx:xx:xx:xx:xx" is the MAC address you want to filter

7. Filter by HTTP status code:
"http.response.status_code == 200" to show only packets with a status code of 200

8. Filter by HTTP method:
"http.request.method == GET" to show only packets with a GET method. You can substitute GET with other HTTP methods such as POST, PUT, DELETE, etc

9. Filter by HTTP URI:
"http.request.uri contains 'example.com'" to show only packets that have a URI containing "example.com". You can substitute "example.com" with any other URI string

10. Filter by HTTP response code:
"http.response.code == 404" to show only packets with a 404 response code

11. Filter by HTTP cookie:
"http.cookie contains 'sessionid'" to show only packets that contain a cookie with the name "sessionid"

12. Filter by TCP flags:
"tcp.flags.syn == 1" to show only packets with the SYN flag set. You can substitute SYN with any other TCP flag, such as ACK, RST, FIN, URG, or PSH

13. Filter by packet size:
"frame.len > 1000" to show only packets larger than 1000 bytes.

14. Filter by DNS domain name:
"dns.qry.name contains 'example.com'" to show only DNS packets that have a domain name containing "example.com". You can substitute "example.com" with any other domain name

15. Filter by TLS handshake type:
"tls.handshake.type == 1" to show only packets with a TLS handshake type of ClientHello
```

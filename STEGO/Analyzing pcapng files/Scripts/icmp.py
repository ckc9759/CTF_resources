import pyshark

capture = pyshark.FileCapture("icmp.pcapng", display_filter="icmp")

# Mergin flag from the ICMP ping rq data
flag = b""
for packet in capture:
    try:
        data = bytes.fromhex(packet.icmp.data)
        flag += data
    except AttributeError:
        continue
capture.close()

print(flag.decode())

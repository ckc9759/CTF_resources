import pyshark
import binascii
import io
cap = pyshark.FileCapture("btle.pcap", display_filter="btatt.opcode == 0x16")

flag = io.BytesIO()
for packet in cap:
	offset = int(packet.btatt.offset)
	flag.seek(offset)

	data = packet.btatt.value.replace(":", "")
	data = binascii.unhexlify(data)

	flag.write(data)

flag.seek(0)
flag.write(b"pb")

print(flag.getvalue())

cap.close()

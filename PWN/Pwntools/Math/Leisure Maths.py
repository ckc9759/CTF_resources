# nc chals.tuctf.com 30202

import telnetlib

HOST = 'chals.tuctf.com'
PORT = 30202

tn = telnetlib.Telnet(HOST,PORT)

i = 0
while True:
	i += 1
	query = tn.read_until(b"Answer: ").decode()
	if 'TUCTF' in query:
		print(query)
		break
	query = query[:-8]
	idxs = [i for i, ch in enumerate(query) if ch == '\n']
	if len(idxs) > 1:
		query = query[idxs[-2]+1:]
	print(i, query)

	resp = f'{int(eval(query))}\n'
	print(f'Ans: {resp}')

	tn.write(resp.encode())
	tn.read_until(b"Correct!")

#----------------------------------------------------------------------------------

from pwn import *
from tqdm import tqdm

r = remote("chals.tuctf.com", 30202)

for i in tqdm(range(1000)):
    eq = r.recvline().strip()
    if b"TUCTF" in eq:
        print(eq)
        r.interactive()
    elif b"import" in eq:
        continue
    else:
        res = eval(eq)
        r.sendlineafter("Answer: ", str(res))
        resdata = r.recvline().strip()
        if b"TUCTF" in resdata:
            print(resdata)

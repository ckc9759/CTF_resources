from pwn import *

conn = remote("calculator.ctf.cert.unlp.edu.ar", 15002)

while True:

    try:

        rec = conn.recv()

        q = rec.strip().split(b"\n")[-1]

        a = eval(q)

        s = str.encode(str(a))



        print(f"[+] question={q} ans={s}")



        conn.send(s)

    except Exception as e:

        print(f"[-] Except: {rec}")

       

#3912 - 669 * 2655 + 7636 * 6677
#Answer: 


from pwn import *

def main():
   p=remote('chals.tuctf.com', 30202)
   
   bool flag=TRUE;
   
   while flag:
	   # challenge = p.recvuntil(b'\n')[:-1].strip()
	   challenge = p.recvuntil(b'\n').strip()
	   solution = int(util.safeeval.expr(challenge))
	   p.recvuntil(b'Answer: ')
	   p.sendline(str(solution).encode())
	   # log.info('Challenge {}: {} = {}'.format(i, challenge.decode(), solution))
	   p.interactive()
	   p.recvuntil(b'Correct!')
if __name__ == '__main__':
    main()

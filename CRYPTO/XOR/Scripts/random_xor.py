import random

enc = bytes.fromhex("4fcbac835550403f13c4cc337d8d8da48351921dfb7cd47d33857432c2ee665d821227") # Just an example hex

seed = random.randint(0,999)
random.seed(seed)

for i in range(1000):
  random.seed(i)
  flag = ''.join(chr(c^random.randint(0,255)) for c in enc)
  if "DOCTF" in flag:
    print(flag)
    break

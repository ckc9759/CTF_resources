import random

enc = bytes.fromhex("4ec5f3eabac8335504") # Just an example hex

seed = random.randint(0,999)
random.seed(seed)

for i in range(1000):
  random.seed(i)
  flag = ''.join(chr(c^random.randint(0,255)) for c in enc)
  if "DOCTF" in flag:
    print(flag)
    break

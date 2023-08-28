from scipy.io import wavfile
from math import ceil

# Reading the data
rate, data = wavfile.read('fl4g.wav')

# Storing amplitude as binary data
bits = ""
for amp in data:
    bits += str(ceil(amp)) # '0' if 0.0  |  '1' if 0.0 < amp < 1.0

# Decoding binary string to ascii
ascii_str = ''
for i in range(0, len(bits), 8):
    ascii_code = int(bits[i:i+8], 2)
    ascii_str += chr(ascii_code)

flag = ascii_str[0:21]               # Only keeping the first occurence of the flag
flag = flag.replace('U+1F5B1', '🖱') # U+1F5B1 is the mouse emoji : 🖱
print('[+] Flag :', flag)

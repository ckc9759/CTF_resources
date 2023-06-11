'''
import wave

with wave.open("chall.wav", "rb") as wav:
    format = wav.getparams()
    frames = wav.readframes(format[3])
    wavs = list(frames)
    lsb = ''.join([format(sample)[-1] for sample in wavs])
    print(lsb)
    flag = lsb[lsb.index('1'):]
    print(int(flag, 2))
    
'''
#!/usr/bin/python
import wave
from scipy.io.wavfile import read

w = wave.open('chall.wav', 'r')
print('n of channels:')
print(w.getnchannels())

n = w.getnframes()
print('n of frames:')
print(n)
frames = w.readframes(n)
print('len(frames):')
print(len(frames))

(fs, x) = read('chall.wav')
print(fs)
print(len(x.shape)) 
print(x[:,0])
print(x[:,1])

c1 = x[:,0]
c2 = x[:,1]
d = []
for a, b in zip(c1, c2):
   d.append(b - a)
print(d[0:100])

out = open('result', 'wb')
for t in d: out.write(chr(t))
out.close()

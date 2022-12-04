from PIL import Image
from pyzbar.pyzbar import decode

for i in range (0,28):
  data = decode(Image.open('image-{}.png'.format(i)))
  final = data[0].data
  print(final.decode())

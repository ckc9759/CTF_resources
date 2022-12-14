from PIL import Image

# Fotoğraf dosyasını oku
foto = Image.open('fotograf.png')

# Alpha kanalını ayır
alpha = foto.split()[3]

# Alpha kanalındaki verileri oku
veriler = alpha.getdata()

# Verileri ASCII karakterlerine dönüştür
ascii_veriler = [chr(x) for x in veriler]
# ASCII verilerini ekrana yaz
#print(''.join(ascii_veriler))
x = ''.join(ascii_veriler)
x = x.replace("ÿ","")
print(x)

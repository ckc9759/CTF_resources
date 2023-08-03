from PIL import Image
import random

random.seed(1678519928.9423187)

flag_matrix = (img := Image.open('pixelite.png')).load()
w, h = img.size

for i in range(w):
    for j in range(h):
        flag_matrix[i, j] = tuple(
            map(
                lambda x: x ^ random.randint(0, 255),
                flag_matrix[i, j]
            )
        )


img.save('decrypted_flag.png')

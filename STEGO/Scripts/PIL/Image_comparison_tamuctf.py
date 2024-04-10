import os
from PIL import Image
import imagehash

static_image = Image.open("image.jpg")
static_hash = imagehash.phash(static_image)

directory = "/home/user/fuzzy/flickr30k_images"

output_file = "comparison_results.txt"

with open(output_file, "w") as f:
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            filepath = os.path.join(directory, filename)
            
            image = Image.open(filepath)
            image_hash = imagehash.phash(image)
            
            hamming_distance = static_hash - image_hash
            
            if hamming_distance < 15:
                f.write(f"Image: {filename}, Hamming distance: {hamming_distance}\n")

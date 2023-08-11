#!/usr/bin/env python3

from PIL import Image
from webcolors import rgb_to_name

hmap = {}
hmap[('magenta', 'red', 'lime', 'yellow', 'blue', 'cyan')] = 'A'
hmap[('red', 'magenta', 'lime', 'yellow', 'blue', 'cyan')] = 'B'
hmap[('red', 'lime', 'magenta', 'yellow', 'blue', 'cyan')] = 'C'
hmap[('red', 'lime', 'yellow', 'magenta', 'blue', 'cyan')] = 'D'
hmap[('red', 'lime', 'yellow', 'blue', 'magenta', 'cyan')] = 'E'
hmap[('red', 'lime', 'yellow', 'blue', 'cyan', 'magenta')] = 'F'
hmap[('lime', 'red', 'yellow', 'blue', 'cyan', 'magenta')] = 'G'
hmap[('lime', 'yellow', 'red', 'blue', 'cyan', 'magenta')] = 'H'
hmap[('lime', 'yellow', 'blue', 'red', 'cyan', 'magenta')] = 'I'
hmap[('lime', 'yellow', 'blue', 'cyan', 'red', 'magenta')] = 'J'
hmap[('lime', 'yellow', 'blue', 'cyan', 'magenta', 'red')] = 'K'
hmap[('yellow', 'lime', 'blue', 'cyan', 'magenta', 'red')] = 'L'
hmap[('yellow', 'blue', 'lime', 'cyan', 'magenta', 'red')] = 'M'
hmap[('yellow', 'blue', 'cyan', 'lime', 'magenta', 'red')] = 'N'
hmap[('yellow', 'blue', 'cyan', 'magenta', 'lime', 'red')] = 'O'
hmap[('yellow', 'blue', 'cyan', 'magenta', 'red', 'lime')] = 'P'
hmap[('blue', 'yellow', 'cyan', 'magenta', 'red', 'lime')] = 'Q'
hmap[('blue', 'cyan', 'yellow', 'magenta', 'red', 'lime')] = 'R'
hmap[('blue', 'cyan', 'magenta', 'yellow', 'red', 'lime')] = 'S'
hmap[('blue', 'cyan', 'magenta', 'red', 'yellow', 'lime')] = 'T'
hmap[('blue', 'cyan', 'magenta', 'red', 'lime', 'yellow')] = 'U'
hmap[('cyan', 'blue', 'magenta', 'red', 'lime', 'yellow')] = 'V'
hmap[('cyan', 'magenta', 'blue', 'red', 'lime', 'yellow')] = 'W'
hmap[('cyan', 'magenta', 'red', 'blue', 'lime', 'yellow')] = 'X'
hmap[('cyan', 'magenta', 'red', 'lime', 'blue', 'yellow')] = 'Y'
hmap[('cyan', 'magenta', 'red', 'lime', 'yellow', 'blue')] = 'Z'
hmap[('black', 'white', 'white', 'black', 'black', 'white')] = '.'
hmap[('white', 'black', 'black', 'white', 'white', 'black')] = ','
hmap[('black', 'black', 'black', 'black', 'black', 'black')] = ' '
hmap[('white', 'white', 'white', 'white', 'white', 'white')] = ' '
hmap[('black', 'black', 'black', 'black', 'black', 'black')] = ' '
hmap[('white', 'white', 'white', 'white', 'white', 'white')] = ' '
hmap[('black', 'gray', 'white', 'black', 'gray', 'white')] = '0'
hmap[('gray', 'black', 'white', 'black', 'gray', 'white')] = '1'
hmap[('gray', 'white', 'black', 'black', 'gray', 'white')] = '2'
hmap[('gray', 'white', 'black', 'gray', 'black', 'white')] = '3'
hmap[('gray', 'white', 'black', 'gray', 'white', 'black')] = '4'
hmap[('white', 'gray', 'black', 'gray', 'white', 'black')] = '5'
hmap[('white', 'black', 'gray', 'gray', 'white', 'black')] = '6'
hmap[('white', 'black', 'gray', 'white', 'gray', 'black')] = '7'
hmap[('white', 'black', 'gray', 'white', 'black', 'gray')] = '8'
hmap[('black', 'white', 'gray', 'white', 'black', 'gray')] = '9'

image = Image.open("attachments/hexhuebad.png")
width, height = image.size
pixels = image.load()

color = []
colors = []
texts = ''

counter = 0
for x in range(20, width-30, 10):
    for y in range(10, height-10, 10):
        color.append(rgb_to_name(pixels[x, y]))
    counter += 1
    if counter == 2:
        counter = 0
        colors.append(color)
        color = []

for color in colors:
    color[0], color[1], color[2], color[3], color[4],  color[5] = color[0], color[3], color[1], color[4], color[2], color[5]
    try:
        texts += hmap[tuple(color)]
    except:
        texts += '_'

print(texts)

#Thank you

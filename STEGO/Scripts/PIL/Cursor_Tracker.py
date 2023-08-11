from PIL import Image, ImageDraw
from PIL import GifImagePlugin
import math

def get_position(img):
    data = img.load()
    for y in range(1, img.height):
        for x in range(1, img.width):
            r, g, b = data[x,y]
            if r < 0.1:
                return (x,y)
    return (-1,-1)

def dist(p0, p1):
    dx = p0[0] - p1[0]
    dy = p0[1] - p1[1]
    return math.sqrt(dx*dx+dy*dy)

prev = (0,0)
reset = False
index = 0
with Image.open("ancient_scrawls.gif") as image:
    out = Image.new(mode="RGB", size=(image.width, image.height))
    out1 = ImageDraw.Draw(out)
    for frame in range(0, image.n_frames):
        if reset:
            out = Image.new(mode="RGB", size=(image.width, image.height))
            out1 = ImageDraw.Draw(out)
            reset = False

        image.seek(frame)
        frame_img = image.convert("RGB")
        pos = get_position(frame_img)

        if prev != (-1,-1) and pos != (-1, -1):
            out1.line([prev, pos])

        if (dist(pos,prev) > 80 and prev[0] > pos[0]):
            out.save("out_" + str(frame) + ".png")
            index = index + 1
            reset = True
        prev = pos

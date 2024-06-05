from PIL import Image
from mouse import mouse_events
import os

img = Image.new('RGB', (10000, 10000), color='white')
canvas = img.load()

# Start the cursor in the middle of the canvas
mouse_x = 5000
mouse_y = 5000

def offset(hex) -> int:
    if hex == 0x0100:
        return +1
    if hex == 0x0200:
        return +2
    if hex == 0xffff:
        return -1
    if hex == 0xfeff:
        return -2
    if hex == 0xfdff:
        return -3

    return 0

for data in mouse_events:
    # Get the left mouse button status
    left_button_pressed = data[0] & 0b00000001

    # Get the mouse movement in x and y
    x_offset = offset(data[1])
    y_offset = offset(data[2])

    mouse_x += x_offset
    mouse_y += y_offset

    if left_button_pressed:
        # These two for loops are to make the pixels thicker
        for i in range(5):
            for j in range(5):
                # Write a black pixel on the canvas
                canvas[round(mouse_x) + i, round(mouse_y) + j] = (0, 0, 0)

# Save the image to disk
img.save("final.png")
os.system('nsxiv final.png')

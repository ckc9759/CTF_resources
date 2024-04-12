from PIL import Image

mouse_events = [(0x80, 0x01, 0xfd), (0x80, 0x01, 0xfe), ... (0x80, 0xff, 0xfa)]

# Make the image big because we don't know how long the message is
img = Image.new('RGB', (10000, 10000), color='white')
canvas = img.load()

# Start the cursor in the middle of the canvas
mouse_x = 5000
mouse_y = 5000

for data in mouse_events:
    # Get the left mouse button status
    left_button_pressed = data[0] & 0b00000001

    # Get the mouse movement in x and y
    x_offset = int.from_bytes(data[1:2], "big", signed=True)
    y_offset = int.from_bytes(data[2:3], "big", signed=True)

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

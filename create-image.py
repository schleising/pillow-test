from PIL import Image, ImageDraw, ImageFont

font = ImageFont.truetype("Roboto/Roboto-Regular.ttf", 48)
im = Image.new("RGB", (200, 200), "green")
d = ImageDraw.Draw(im)
d.line(((0, 100), (200, 100)), "blue")
d.line(((100, 0), (100, 200)), "blue")
d.text((100, 100), "Quick", fill="red", anchor='ms', font=font)

im.show()

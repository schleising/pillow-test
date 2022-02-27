from pathlib import Path

from PIL import Image

im = Image.open(Path('input/test_image01.jpg'))

print(im.format, im.size, im.mode)

im = im.rotate(270)

im.show()

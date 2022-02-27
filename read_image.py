from pathlib import Path

from PIL import Image

with Image.open(Path('input/test_image01.jpg')) as im:
    print(im.format, im.size, im.mode)

    r, g, b = im.split()
    im = Image.merge('RGB', (b, r, g))

    im.show()

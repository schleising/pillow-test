from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

scores = {
    1: 0,
    2: 2,
    3: 11,
    4: 14,
    5: 10,
    6: 6,
}

FULL_IMAGE_SIZE = (750, 500)
GUESS_DISTRIBUTION_SIZE = (475, 50)
BAR_SCORE_SIZE = (750, 70)
SCORE_SIZE = (50, 70)
BAR_SIZE = (700, 70)

textFont = ImageFont.truetype('Roboto/Roboto-Black.ttf', 45)
scoreFont = ImageFont.truetype('Roboto/Roboto-Regular.ttf', 45)

gdImage = Image.new('RGB', GUESS_DISTRIBUTION_SIZE, 'white')
gdDraw = ImageDraw.Draw(gdImage)

gdAnchorPos = tuple(dim // 2 for dim in GUESS_DISTRIBUTION_SIZE)

gdDraw.text(gdAnchorPos, 'GUESS DISTRIBUTION', fill='black', anchor='mm', font=textFont)

# gdImage.show()

imageList = []
imageList.append(gdImage)

maximumCount = max(scores.values())

for score, count in scores.items():
    barImage = Image.new('RGB', BAR_SCORE_SIZE, 'white')
    barDraw = ImageDraw.Draw(barImage)

    scoreAnchorPos = tuple(dim // 2 for dim in SCORE_SIZE)

    barDraw.text(scoreAnchorPos, str(score), fill='black', anchor='mm', font=scoreFont)

    if count != 0:
        barLength = (BAR_SIZE[0] * count / maximumCount) - 5

        barDraw.rectangle((50, 5, barLength + SCORE_SIZE[0], BAR_SIZE[1] - 5), fill='grey')
        countText = str(count)
        countLength = scoreFont.getlength(countText)
        countAnchorPos = (barLength + SCORE_SIZE[0] - countLength // 2 - 10, BAR_SIZE[1] // 2)

        barDraw.text(countAnchorPos, countText, fill='white', anchor='mm', font=scoreFont)

    # barImage.show()

    imageList.append(barImage)

fullImage = Image.new('RGB', FULL_IMAGE_SIZE, 'white')

imageBoxHeight = FULL_IMAGE_SIZE[1] // len(imageList)
imageBoxCentrePoint = imageBoxHeight // 2

for count, image in enumerate(imageList):
    imageLeft = (fullImage.size[0] - image.size[0]) // 2
    imageTop = (count * imageBoxHeight) + imageBoxCentrePoint - (image.size[1] // 2)
    imageRight = imageLeft + image.size[0]
    imageBottom = imageTop + image.size[1]

    fullImage.paste(image, (imageLeft, imageTop, imageRight, imageBottom))

fullImage.save(Path('output/gd.png'), 'PNG')

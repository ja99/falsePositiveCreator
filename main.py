import glob
import random

from PIL import Image, ImageDraw, ImageFilter

N_IMAGES = 10


false_positive_imgs = []
for path in glob.iglob(f'false_positive_imgs/**/*.png', recursive=True):
    false_positive_imgs.append(path)

positive_imgs = []
for path in glob.iglob(f'positive_imgs/**/*.png', recursive=True):
    positive_imgs.append(path)


for i in range(N_IMAGES):
    p_i = random.randint(0, len(positive_imgs)-1)
    positive = Image.open(positive_imgs[p_i])

    f_i = random.randint(0, len(false_positive_imgs)-1)
    false_positive = Image.open(false_positive_imgs[f_i])

    if false_positive.width <= positive.width or false_positive.height <= positive.height:
        continue

    pos_x = random.randint(0, false_positive.width - positive.width)
    pos_y = random.randint(0, false_positive.height - positive.height)

    out = false_positive.copy()
    out.paste(positive, (pos_x, pos_y))
    out.save(f"output_imgs/{i}.png", quality=100)

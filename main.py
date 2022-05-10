from PIL import Image, ImageDraw, ImageFilter

false_positive_img = Image.open('false_positive_imgs/white.png')
positive_img = Image.open('positive_imgs/woman.png')

out = false_positive_img.copy()
out.paste(positive_img, (30,30))
out.save("output_imgs/out.png", quality=100)
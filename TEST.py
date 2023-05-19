from PIL import Image


with Image.open('ии2.jpg') as im:
    pixels = im.load()

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            r, g, b = pixels[i, j]
            pixels[i, j] = 0, g if 51 < g < 200 else 0, 0

    im.save("hh.png")
from PIL import Image

im  = Image.open('pillow.JPG')

print(im.filename)
print(im.size)
print(im.width, im.height)
print(im.format)
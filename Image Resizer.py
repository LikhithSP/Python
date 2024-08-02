from PIL import Image

im = Image.open('')
print(im.size)
new_size = im.resize((400, 400))
new_size.show()

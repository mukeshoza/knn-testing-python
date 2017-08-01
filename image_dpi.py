from PIL import Image
with Image.open('2.jpg') as img:
    width, height = img.size
print(img.size)


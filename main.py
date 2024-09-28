from PIL import Image

image_path = "images\image2.bmp"
target_color = (131, 0, 0)
ring_color = (0, 255, 255)

count = 0
with Image.open(image_path) as img:
    # print(img.getcolors())
    for pixel in img.getdata():
        if pixel == target_color:
            count += 1

print(count)
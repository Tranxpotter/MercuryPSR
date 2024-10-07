from PIL import Image
import os

folder_name = "south_pole_PSR"
filenames = os.listdir(f"data_files/{folder_name}")

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (2560, 1440)

CAPTURE_CORD = (775, 0)
MOUSE_REFERENCE_POINT = (100, 100)
SCROLL = 192
SCROLL_INTERVAL = 0.2

HORIZONTAL_SCROLL = 9
VERTICAL_SCROLL = 7

CAPTURE_SIZE = CAPTURE_WIDTH, CAPTURE_HEIGHT = (SCROLL * HORIZONTAL_SCROLL, SCROLL * VERTICAL_SCROLL)




max_row = 0
min_row = 0
max_column = 0
min_column = 0
for filename in filenames:
    info, ext = filename.split(".")
    row, column = map(int, info.split("_"))
    max_row = max(max_row, row)
    min_row = min(min_row, row)
    max_column = max(max_column, column)
    min_column = min(min_column, column)


print(max_row, min_row, max_column, min_column)

size = (max_column - min_column + 1) * CAPTURE_WIDTH, (max_row - min_row + 1) * CAPTURE_HEIGHT
print(size)
background = Image.new("RGB", size, "white")

for filename in filenames:
    info, ext = filename.split(".")
    row, column = map(int, info.split("_"))
    row, column = row - min_row, column - min_column
    pos = column * CAPTURE_WIDTH, row * CAPTURE_HEIGHT

    with Image.open(f"data_files/{folder_name}/{filename}") as img:
        background.paste(img, pos)

background.save("data_files/full_images/south_pole_PSR.png")




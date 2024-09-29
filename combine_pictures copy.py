from PIL import Image
import os


filenames = os.listdir("data_files/north_pole_PSR")

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

size = (max_row - min_row + 1) * CAPTURE_HEIGHT, (max_column - min_column + 1) * CAPTURE_WIDTH
print(size)
# background = Image.new("RGB", size, "white")

max_img_x, max_img_y = 0, 0
for filename in filenames:
    info, ext = filename.split(".")
    row, column = map(int, info.split("_"))
    row, column = row - min_row, column - min_column
    pos = column * CAPTURE_WIDTH, row * CAPTURE_HEIGHT
    max_img_x = max(max_img_x, pos[0])
    max_img_y = max(max_img_y, pos[1])
#     with Image.open(f"data_files/north_pole_radio/{filename}") as img:
#         background.paste(img, pos)
print(max_img_x, max_img_y)
# background.save("test.png")



-1, 5
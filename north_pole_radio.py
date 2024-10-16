import os
import math
from PIL import Image

FILE_PATH = "data_files/north_pole_radio/"

SCROLL = 192
HORIZONTAL_SCROLL = 9
VERTICAL_SCROLL = 7
CAPTURE_SIZE = CAPTURE_WIDTH, CAPTURE_HEIGHT = (SCROLL * HORIZONTAL_SCROLL, SCROLL * VERTICAL_SCROLL)


# REMINDER: Image cord is (row, column) which corresponds to (y, x) 
#           While cord is (x, y)

CENTER_IMAGE = (0, 0)
CENTER_CORD = (471, 715)

RING_INFO = {
    89:((-2, 0), (699, 859)),
    88:((-4, 0), (673, 985)),
    87:((-6, 0), (671, 1116)),
    86:((-8, 0), (646, 1246)),
    85:((-9, 0), (704, 31)),
    84:((-11, 0), (616, 157)),
    83:((-13, 0), (638, 282)),
    82:((-15, 0), (664, 405)),
    81:((-17, 0), (735, 524)),
    80:((-19, 0), (609, 639))
}


MATCH_RED = 131
EDGE_RED_MATCH = 59

def get_rel_cord(imr:int, imc:int, cord:tuple[int, int]) -> tuple[int, int]:
    '''Get the relative coordinate of a pixel in an image'''
    return (CAPTURE_WIDTH * imc + cord[0] - CENTER_CORD[0], CAPTURE_HEIGHT * imr + cord[1] - CENTER_CORD[1])


def get_dist_from_center(cord:tuple[int, int]) -> float:
    '''Calculate the distance of the relative coordinate from the center'''
    return math.dist((0, 0), cord)


def get_img_rel_cord(imr:int, imc:int) -> tuple[int, int]:
    '''Get the relative coordinate of the top left corner of the image in (x, y)'''
    return (CAPTURE_WIDTH * imc - CENTER_CORD[0], CAPTURE_HEIGHT * imr - CENTER_CORD[1])


def get_corners(imr:int, imc:int) -> list[tuple[int]]:
    '''Get the relative coordinates of the corners of the image'''
    tl = get_img_rel_cord(imr, imc)
    tr = (tl[0] + CAPTURE_WIDTH, tl[1])
    bl = (tl[0], tl[1] + CAPTURE_HEIGHT)
    br = (tl[0] + CAPTURE_WIDTH, tl[1] + CAPTURE_HEIGHT)
    return [tl, tr, bl, br]



def filename_to_img_cord(filename:str):
    '''Returns the image cord as (row, column) given the filename'''
    position_string, _ = filename.split(".")
    row, column = map(lambda x:int(x), position_string.split("_"))
    return row, column

def filename_to_corner_distances(filename:str):
    img_cord = filename_to_img_cord(filename)
    corners = get_corners(*img_cord)
    return list(map(lambda corner:get_dist_from_center(corner), corners))

def img_corners_in_ring(filename:str, ring_dist:float):
    corner_distances = filename_to_corner_distances(filename)
    return sum(map(lambda dist:dist <= ring_dist, corner_distances))



def get_ring_dist(ring_num:int):
    ring_img_cord, ring_cord = RING_INFO[ring_num]
    ring_rel_cord = get_rel_cord(*ring_img_cord, ring_cord)
    ring_dist = get_dist_from_center(ring_rel_cord)
    return ring_dist


def cal(ring_num:int):
    filenames = os.listdir(FILE_PATH)
    
    ring_dist = get_ring_dist(ring_num)
    
    images_corners_in_ring =  map(lambda filename:img_corners_in_ring(filename, ring_dist), filenames)

    count = 0
    for search_img_name, corners_in_ring in zip(filenames, images_corners_in_ring):
        # print(f"{search_img_name}:{corners_in_ring}")
        if corners_in_ring == 0:
            continue
        with Image.open(f"{FILE_PATH}{search_img_name}") as img:
            if corners_in_ring == 4:
                for pixel in img.getdata(0):
                    if pixel == MATCH_RED:
                        count += 1
            else:
                img_cord = filename_to_img_cord(search_img_name)
                img_rel_cord = get_img_rel_cord(*img_cord)
                
                for index, pixel in enumerate(img.getdata(0)):
                    if pixel != MATCH_RED:
                        continue
                    row = index // CAPTURE_WIDTH
                    column = index % CAPTURE_WIDTH
                    pixel_rel_cord = (img_rel_cord[0] + column, img_rel_cord[1] + row)
                    pixel_dist = get_dist_from_center(pixel_rel_cord)
                    if pixel_dist <= ring_dist:
                        count += 1
    
    return count



import time


if __name__ == "__main__":
    pixel_length = 2000/121
    pixel_area = pixel_length * pixel_length
    rings = [i for i in range(89, 79, -1)]
    for ring in rings:
        start_time = time.time()
        result = cal(ring)
        print(f"Ring: {ring}, result: {result}, area: {result * pixel_area}, time spent: {time.time() - start_time}")

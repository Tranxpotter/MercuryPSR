import pyautogui
import keyboard
import time
import playsound

pyautogui.PAUSE = 0

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (2560, 1440)

CAPTURE_SIZE = (1732, 1368)
CAPTURE_CORD = (775, 0)
SAFE_POINT = (100, 100)
MOUSE_DELAY = 0.1
DRAG_DURATION = 1

SCROLL = 192

save_path = "test/"
lat_lon_path = "lat_lon_log/"

row = 0
column = 0
cont_capturing = False
cont_capturing_direction = None



def drag_right():
    global column
    start_x = CAPTURE_SIZE[0] + CAPTURE_CORD[0]
    end_x = CAPTURE_CORD[0]
    pyautogui.moveTo(start_x, SCREEN_HEIGHT//2)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseDown()
    time.sleep(MOUSE_DELAY)
    pyautogui.moveTo(end_x, SCREEN_HEIGHT//2, duration=DRAG_DURATION)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseUp()
    column += 1

def drag_left():
    global column
    start_x = CAPTURE_CORD[0]
    end_x = CAPTURE_SIZE[0] + CAPTURE_CORD[0]
    pyautogui.moveTo(start_x, SCREEN_HEIGHT//2)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseDown()
    time.sleep(MOUSE_DELAY)
    pyautogui.moveTo(end_x, SCREEN_HEIGHT//2, duration=DRAG_DURATION)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseUp()
    column -= 1

def drag_up():
    global row
    start_y = CAPTURE_CORD[1]
    end_y = CAPTURE_CORD[1] + CAPTURE_SIZE[1]
    pyautogui.moveTo(SCREEN_WIDTH//2, start_y)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseDown()
    time.sleep(MOUSE_DELAY)
    pyautogui.moveTo(SCREEN_WIDTH//2, end_y, duration=DRAG_DURATION)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseUp()
    row -= 1

def drag_down():
    global row
    start_y = CAPTURE_CORD[1] + CAPTURE_SIZE[1]
    end_y = CAPTURE_CORD[1]
    pyautogui.moveTo(SCREEN_WIDTH//2, start_y)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseDown()
    time.sleep(MOUSE_DELAY)
    pyautogui.moveTo(SCREEN_WIDTH//2, end_y, duration=DRAG_DURATION)
    time.sleep(MOUSE_DELAY)
    pyautogui.mouseUp()
    row += 1


def capture():
    pyautogui.moveTo(*SAFE_POINT)
    pyautogui.screenshot(f"{save_path}{row}_{column}.bmp", (CAPTURE_CORD[0], CAPTURE_CORD[1], CAPTURE_SIZE[0], CAPTURE_SIZE[1]))
    pyautogui.screenshot(f"{lat_lon_path}{row}_{column}.jpg", (CAPTURE_CORD[0], CAPTURE_CORD[1], CAPTURE_SIZE[0], CAPTURE_SIZE[1]))


def to_safe_point():
    pyautogui.moveTo(*SAFE_POINT)

def toggle_cont_capturing():
    global cont_capturing
    capture()
    cont_capturing = not cont_capturing

def get_change_cont_capturing_direction(direction:str):
    global cont_capturing_direction
    def change_cont_capturing_direction():
        global cont_capturing_direction
        cont_capturing_direction = direction
    return change_cont_capturing_direction

#Normal mode hotkeys
keyboard.add_hotkey("a", drag_left)
keyboard.add_hotkey("d", drag_right)
keyboard.add_hotkey("w", drag_up)
keyboard.add_hotkey("s", drag_down)
keyboard.add_hotkey("space", capture)
keyboard.add_hotkey("1", to_safe_point)

#Cont capturing hotkeys
keyboard.add_hotkey("t", lambda:get_change_cont_capturing_direction("up"))
keyboard.add_hotkey("f", lambda:get_change_cont_capturing_direction("left"))
keyboard.add_hotkey("g", lambda:get_change_cont_capturing_direction("down"))
keyboard.add_hotkey("h", lambda:get_change_cont_capturing_direction("right"))
keyboard.add_hotkey("c", toggle_cont_capturing)

keyboard.add_hotkey("e", pyautogui.mouseDown)
keyboard.add_hotkey("q", pyautogui.mouseUp)

if __name__ == "__main__":
    print("Starting program, please input the starting values of:")
    row = int(input("row: "))
    column = int(input("column: "))
    
    # Match cursor top right corner LAT and LON if necessary #
    
    while True:
        while cont_capturing:
            if cont_capturing_direction == "up":
                drag_up()
            elif cont_capturing_direction == "left":
                drag_left()
            elif cont_capturing_direction == "right":
                drag_right()
            elif cont_capturing_direction == "down":
                drag_down()
            capture()





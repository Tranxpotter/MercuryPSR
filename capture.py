import pyautogui
import keyboard
import pynput
import time

save_path = "data_files/images/"

# Usage: Normal mode - WASD for movement, space to capture screen
#        Continuous mode - WASD for changing movement direction, shift to capture and move
#        Press E to switch betweeen normal and continuous mode, Press Q to toggle the continuous capture

pyautogui.FAILSAFE = False

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (2560, 1440)

CAPTURE_CORD = (775, 0)
MOUSE_REFERENCE_POINT = (100, 100)
SCROLL = 192
SCROLL_INTERVAL = 0.2

HORIZONTAL_SCROLL = 9
VERTICAL_SCROLL = 7

CAPTURE_SIZE = CAPTURE_WIDTH, CAPTURE_HEIGHT = (SCROLL * HORIZONTAL_SCROLL, SCROLL * VERTICAL_SCROLL)



# lat_lon_path = "data_files/south_pole_log/"


class Capture:
    def __init__(self, row:int = 0, column:int = 0) -> None:
        self.row = row
        self.column = column
        self.cont_capturing = False
        self.cont_capturing_mode = False
        self.cont_capturing_direction = None
        
        kb = pynput.keyboard.GlobalHotKeys(
            {
                "w" : lambda:self.on_movement_key("w"), 
                "s" : lambda:self.on_movement_key("s"),
                "a" : lambda:self.on_movement_key("a"),
                "d" : lambda:self.on_movement_key("d"),
                " " : self.capture,
                "q":self.toggle_cont_capturing,
                "e":self.toggle_cont_capturing_mode,
                "r":self.display
            }
        )
        kb.start()
        # keyboard.add_hotkey("w", lambda:self.on_movement_key("w"))
        # keyboard.add_hotkey("s", lambda:self.on_movement_key("s"))
        # keyboard.add_hotkey("a", lambda:self.on_movement_key("a"))
        # keyboard.add_hotkey("d", lambda:self.on_movement_key("d"))
        # keyboard.add_hotkey("space", self.capture)
        # keyboard.add_hotkey("q", self.toggle_cont_capturing)
        # keyboard.add_hotkey("e", self.toggle_cont_capturing_mode)
        # keyboard.add_hotkey("r", self.display)
        
        self.key_direction_match = {
            "w":self.up, 
            "s":self.down,
            "a":self.left, 
            "d":self.right
        }
        
        cont = False
        
        def on_continue(key):
            nonlocal cont
            if key == pynput.keyboard.Key.shift:
                cont = True
                        
        l = pynput.keyboard.Listener(on_continue)
        l.start()
        while True:
            while self.cont_capturing:
                if not self.cont_capturing_direction:
                    continue
                self.key_direction_match[self.cont_capturing_direction]()
                
                
                while not cont:
                    pass
                
                cont = False
                # keyboard.wait("shift")
                self.capture()
                time.sleep(1)
    
    
    
    def toggle_cont_capturing_mode(self):
        self.cont_capturing_mode = not self.cont_capturing_mode
    
    def toggle_cont_capturing(self):
        self.capture()
        self.cont_capturing = not self.cont_capturing
    
    def on_movement_key(self, key:str):
        if self.cont_capturing_mode:
            self.cont_capturing_direction = key
        else:
            self.key_direction_match[key]()

    def up(self):
        pyautogui.press("up", presses=VERTICAL_SCROLL, interval=SCROLL_INTERVAL)
        self.row -= 1
    
    def down(self):
        pyautogui.press("down", presses=VERTICAL_SCROLL, interval=SCROLL_INTERVAL)
        self.row += 1

    def left(self):
        pyautogui.press("left", presses=HORIZONTAL_SCROLL, interval=SCROLL_INTERVAL)
        self.column -= 1

    def right(self):
        pyautogui.press("right", presses=HORIZONTAL_SCROLL, interval=SCROLL_INTERVAL)
        self.column += 1

    def capture(self):
        pyautogui.moveTo(*MOUSE_REFERENCE_POINT)
        pyautogui.screenshot(f"{save_path}{self.row}_{self.column}.bmp", (CAPTURE_CORD[0], CAPTURE_CORD[1], CAPTURE_SIZE[0], CAPTURE_SIZE[1]))
        #pyautogui.screenshot(f"{lat_lon_path}{self.row}_{self.column}.jpg", (0, 1385, 350, 55))
        
    def display(self):
        print(self.row, self.column)
        
    
    
    
    



if __name__ == "__main__":
    print("Starting program, please input the starting values of:")
    row = int(input("row: "))
    column = int(input("column: "))
    
    Capture(row, column)
    
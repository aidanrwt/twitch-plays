import win32api
import win32con

import time

class Game:

    keymap = {
        'up': 0x30,
        'down': 0x31,
        'left': 0x32,
        'right': 0x33,
        'a': 0x34,
        'b': 0x35,
        'start': 0x36,
        'select': 0x37
    }

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
        time.sleep(0.1)
        win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
        
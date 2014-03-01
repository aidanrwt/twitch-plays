import os
import time
if os.name == 'nt':
    import win32api
    import win32con
else:
    from subprocess import Popen

class Game:

    if os.name == 'nt':
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
    else:
        keymap = {
            'up': ["Up"],
            'down': ["Down"],
            'left': ["Left"],
            'right': ["Right"],
            'a': ["a"],
            'b': ["b"],
            'start': ["Return"]
        }

    def get_valid_buttons(self):
        return [button for button in self.keymap.keys()]

    def is_valid_button(self, button):
        return button in self.keymap.keys()

    def button_to_key(self, button):
        return self.keymap[button]

    def push_button(self, button):
        if os.name == 'nt':
            win32api.keybd_event(self.button_to_key(button), 0, 0, 0)
            time.sleep(.15)
            win32api.keybd_event(self.button_to_key(button), 0, win32con.KEYEVENTF_KEYUP, 0)
        else:
            Popen(["xdotool", "keydown"] + self.button_to_key(button))
            time.sleep(.15)
            Popen(["xdotool", "keyup"] + self.button_to_key(button))

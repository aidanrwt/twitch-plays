import time

from config.config import config
from lib.irc import Irc
from lib.game import Game
from lib.misc import pbutton

class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()

        self.message_buffer = [{'username': '', 'button': ''}] * 10


    def set_message_buffer(self, message):
        chat_height = 10
        self.message_buffer.insert(chat_height - 1, message)
        self.message_buffer.pop(0)


    def run(self):
        last_start = time.time()

        while True:
            new_messages = self.irc.recv_messages(1024)
            
            if not new_messages:
                continue

            for message in new_messages: 
                button = message['message'].lower()
                username = message['username'].lower()

                if not self.game.is_valid_button(button):
                    continue

                print button

                if self.config['start_throttle']['enabled'] and button == 'start':
                    if time.time() - last_start < self.config['start_throttle']['time']:
                        continue

                if button == 'start':
                    last_start = time.time()

                self.set_message_buffer({'username': username, 'button': button})
                pbutton(self.message_buffer)
                self.game.push_button(button)
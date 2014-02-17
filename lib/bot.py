from irc import Irc
from game import Game
from misc import pp, pbot, pbutton

import time

class Bot:

    def __init__(self, config):
        self.config = config
        self.irc = Irc(config)
        self.game = Game()

    def run(self):
        last_start = time.time()

        while True:
            new_messages = self.irc.recv_messages(1024)
            
            if not new_messages:
                continue

            for message in new_messages:      
                button = message['message'].lower()
                username = message['username']

                if not self.game.is_valid_button(button):
                    continue

                if self.config['start_throttle']['enabled'] and button == 'start':
                    if time.time() - last_start < self.config['start_throttle']['time']:
                        continue

                if button == 'start':
                    last_start = time.time()

                pbutton(username, button)
                self.game.push_button(button)


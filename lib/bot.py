from irc import *
from game import *
from misc import *

class bot:

    def __init__(self, config):
        self.config = config
        self.irc = irc(config)
        self.game = game()

    def is_valid_button(self, message):
        valid_buttons = [
            'up', 'down', 'left', 'right',
            'a', 'b', 'start', 'select'
        ]

        if message in valid_buttons:
            return True

    def run(self):
        while True:
            
            # grab newest messages as a list
            new_messages = self.irc.recv_messages(1024)
            
            if new_messages:
                for message in new_messages:
                    #ppi(message['channel'], message['message'], message['username'])

                    if not self.is_valid_button(message['message'].lower()):
                        continue

                    button = message['message'].lower()

                    pbutton(message['username'], button)
                    self.game.push_button(button)


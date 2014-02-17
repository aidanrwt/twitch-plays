import socket
import sys
import re
from misc import *

class irc:

    def __init__(self, config):
        self.config = config
        self.set_socket_object()


    def set_socket_object(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock

        sock.settimeout(10)

        username = self.config['account']['username']
        password = self.config['account']['password']

        server = self.config['irc']['server']
        port = self.config['irc']['port']

        try:
            sock.connect((server, port))
        except:
            pp('Error connecting to server.', 'error')
            sys.exit()

        sock.settimeout(None)

        sock.send('USER %s\r\n' % username)
        sock.send('PASS %s\r\n' % password)
        sock.send('NICK %s\r\n' % username)

        if not self.check_login_status(self.recv()):
            pp('Invalid login.', 'error')
            sys.exit()
        else:
            pp('Login successful!')

        sock.send('JOIN #%s\r\n' % username.lower())
        pp('Joined #%s\n\n' % username.lower())


    def ping(self, data):
        if data[:4] == 'PING':
            pbot('PONG')
            self.sock.send(data.replace('PING', 'PONG'))


    def recv(self, amount=1024):
        return self.sock.recv(amount)

    def recv_messages(self, amount=1024):
        data = self.recv(amount)
        resp = []

        if len(data) == 0:
            pbot('Lost connection, reconnecting.')
            self.set_socket_object()
            self.recv_messages(amount)

        self.ping(data)

        if not self.check_has_message(data):
            return

        else:
            data = filter(None, data.split('\r\n'))
            for line in data:
                info = self.parse_data_for_message(line)
                resp.append(info)

        return resp


    def check_login_status(self, data):
        if re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data):
            return False
        else:
            return True

    def check_has_message(self, data):
        if re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data):
            return True

    def parse_data_for_message(self, data): 
        channel = re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0]
        username = re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0]
        message = re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0].decode('utf8')

        return {
            'channel': channel,
            'username': username,
            'message': message
        }


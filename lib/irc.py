import socket
import sys
import re

from lib.misc import pp, pbot

class Irc:

    socket_retry_count = 0

    def __init__(self, config):
        self.config = config
        self.set_socket_object()

    def set_socket_object(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = sock

        sock.settimeout(10)

        username = self.config['account']['username'].lower()
        password = self.config['account']['password']

        server = self.config['irc']['server']
        port = self.config['irc']['port']

        try:
            sock.connect((server, port))
        except:
            pp('Error connecting to IRC server. (%s:%i) (%i)' % (server, port, self.socket_retry_count + 1), 'error')

            if self.socket_retry_count < 2:
                self.socket_retry_count += 1
                return self.set_socket_object()
            else:
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

        sock.send('JOIN #%s\r\n' % username)
        pp('Joined #%s' % username)

    def ping(self, data):
        if data.startswith('PING'):
            self.sock.send(data.replace('PING', 'PONG'))

    def recv(self, amount=1024):
        return self.sock.recv(amount)

    def recv_messages(self, amount=1024):
        data = self.recv(amount)

        if not data:
            pbot('Lost connection, reconnecting.')
            return self.set_socket_object()

        self.ping(data)

        if self.check_has_message(data):
            return [self.parse_message(line) for line in filter(None, data.split('\r\n'))]

    def check_login_status(self, data):
        if not re.match(r'^:(testserver\.local|tmi\.twitch\.tv) NOTICE \* :Login unsuccessful\r\n$', data): return True

    def check_has_message(self, data):
        return re.match(r'^:[a-zA-Z0-9_]+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+(\.tmi\.twitch\.tv|\.testserver\.local) PRIVMSG #[a-zA-Z0-9_]+ :.+$', data)

    def parse_message(self, data): 
        return {
            'channel': re.findall(r'^:.+\![a-zA-Z0-9_]+@[a-zA-Z0-9_]+.+ PRIVMSG (.*?) :', data)[0],
            'username': re.findall(r'^:([a-zA-Z0-9_]+)\!', data)[0],
            'message': re.findall(r'PRIVMSG #[a-zA-Z0-9_]+ :(.+)', data)[0].decode('utf8')
        }
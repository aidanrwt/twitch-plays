import time
from os import system

def pp(message, mtype='INFO'):
    mtype = mtype.upper()
    print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
    print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, username.lower(), message)

def pbot(message, channel=''):
    if channel: 
        msg = '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, 'BOT', message)
    else: 
        msg = '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), 'BOT', message)

    print msg

def pbutton(message_buffer):
    system('cls')
    print '\n\n'
    print '\n'.join([' {0:<12s} {1:>6s}'.format(message['username'][:12].title(), message['button'].lower()) for message in message_buffer])
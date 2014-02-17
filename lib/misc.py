import time

red = "\033[01;31m{0}\033[00m"
grn = "\033[01;36m{0}\033[00m"
blu = "\033[01;34m{0}\033[00m"
cya = "\033[01;36m{0}\033[00m"
gra = "\033[01;30m{0}\033[00m"


def pp(message, mtype='INFO'):
    mtype = mtype.upper()

    if mtype == "ERROR":
        mtype = red.format(mtype)

    print '[%s] [%s] %s' % (time.strftime('%H:%M:%S', time.gmtime()), mtype, message)

def ppi(channel, message, username):
    print '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, grn.format(username.lower()), message)

def pbot(message, channel=''):
    if channel: msg = '[%s %s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), channel, red.format('BOT'), message)
    else: msg = '[%s] <%s> %s' % (time.strftime('%H:%M:%S', time.gmtime()), red.format('BOT'), message)

    print msg

def pbutton(username, button):
    # buffer_size is the horizontal width of the mesage buffer
    # buffer_left will also just be whitespace to fill the gap
    #
    # the username will be cut short if it's too long to create 
    # a constant width
    #
    # example output with a buffer size of 20 and whitespace 1 -
    # twitch_plays_pacm up
    # twitch_plays_pa down
    # aidraj_           up
    # aidraj_         down

    buffer_size = 20
    buffer_used = 0
    whitespace_size = 1

    buffer_used =  len(button) + whitespace_size
    buffer_left = buffer_size - buffer_used
    
    if buffer_left > len(username):
        # fill the missing space
        whitespace_size += buffer_left - len(username)

    username_end = buffer_left

    username = username[:username_end]

    print '%s%s%s' % (username, ' '*whitespace_size, button)

#    print '[%s] %s pressed %s' % (time.strftime('%H:%M:%S'), gra.format(username), gra.format(button))
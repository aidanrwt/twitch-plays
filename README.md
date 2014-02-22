Twitch Plays
============

Clone of [Twitch Plays Pokemon](http://twitch.tv/twitch_plays_pokemon).



Installation
============

You're going to need to have [pywin32](http://sourceforge.net/projects/pywin32/) installed. If you run into any errors try running this with Python [2.7.x](http://www.python.org/download/releases/2.7/).

Rename `config/config_dist.py` to `config/config.py`, and replace the username/password there with your Twitch username and [OAuth token](http://www.twitchapps.com/tmi/). Feel free to modify the start throttle here aswell.

In your VBA/Emulator, set the controls to the following -

```
Up: 0
Down: 1
Left: 2
Right: 3
Button A: 4
Button B: 5
Start: 6
Select: 7
```

After you've set that up, open up your terminal and type `python serve.py`. If your username/password is wrong you will be notified.

Whilst the script is running make sure you have your emulator in focus as your primary window. If you click onto another window, the script won't work. If you're not able to stay focused on one window as you need to do other things with your computer, you could try running all of this from within a virtual machine.

--


If you have any question or need help, feel free to [message me on Twitch](http://www.twitch.tv/message/compose?to=aidraj_) or send an email to `aidraj0 at gmail dot com`.

You'll need to have VBA in focus for this to work, so your best bet would be to run all of this
from within a VM.

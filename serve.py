#!/usr/bin/env python

# Twitch Plays
# Clone of twitch.tv/twitchplayspokemon
# Written by Aidan Thomson <aidraj0 at gmail dot com>

from config.config import *
import lib.bot as bot

bot = bot.Bot(config).run()


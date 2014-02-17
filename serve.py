#!/usr/bin/env python
# coding: utf8

# Twitch Plays Pokemon
# Clone of twitch.tv/twitchplayspokemon
# Written by Aidan Thomson <aidraj0@gmail.com>

from config.config import *
import lib.bot as bot

bot = bot.bot(config).run()


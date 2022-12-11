# Virtual Fitness Assistant Application
# Developer: Stefan M. Green
# 2019 Dec. Version 1.0.0
#
# Application is designed to encourage development and enthusiasm toward a healthy fitness lifestyle.
# Software will allow user to create a personal profile based on their individual goals and interests.
# Software will create a symbiotic experience where the user can track their progress and set goals.

import eel
from gui.logfile import data_mind
from gui.usersession import flush_session
from gui.voices import hello, listen


eel.init("gui")

# Function flushes user session database upon starting setting values to offline
flush_session()

# Function creates the databases in the even that they are not there
data_mind()

# Greeting function. I Need to figure out flow control.
hello()

# Listener records audio data  from user
listen()

# quick boot
# eel.start("/member.html")


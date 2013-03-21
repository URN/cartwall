# Copyright (c) 2009 - 2013 Thomas Preece
# 
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to 
# the following conditions:
# 
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# 
# You can customize your Cartwall by changing the rest of this file.
# 

# Audio sample rate. You should usually leave this as 44100 unless you know
# you need something different. Note that if your audio files are encoded at a
# different sample rate, they will play back at the wrong speed.
SAMPLERATE = 44100

# Where is the configuration file?
CONFIGFILE = './cartwall.conf'

# Where are the audio files stored? You must add a trailing slash.
AUDIODIR = './'

# What is the extension of the audio files? If all your files are the same
# format, it may be convenient to set this, and then just provide the "audio ID"
# in the configuration file. If you have audio of more than one format, set it
# to blank and provide the extension for each audio file in the config file.
AUDIOEXT = '.ogg'

# Should the audio be streamed from disk (True) or loaded into memory when the
# program starts (False)? Loading into memory is safer, but will result in a
# long start up time, particularly if you use large audio files.
AUDIO_STREAM_FROM_DISK = True

# How many carts do you want per page? If too many carts are specified in the
# configuration file, they will be ignored, but if too few are specified, the
# program will not work.
ROWS = 6
COLS = 6

# Default colors
EMPTY_COLOR = 'black'	# Color of an empty cart
BG_COLOR = 'cyan'		# Default background color
FG_COLOR = 'black'		# Foreground (ie, text) color
PLAY_COLOR = 'green'	# Background color of a playing cart
EOF_COLOR = '#cccccc'	# Flash this color for EOF warning

# How many seconds before the end of the file should we start the EOF warning?
# Set to 0 to disable.
EOF_TIME = 5

# Page buttons. There are five pages; from version 0.2 onwards, the colours are
# specified in the configuration file. For version 0.1 or earlier, the colours
# are defined here. The "HL" (highlight) color is used when for the active page.
LEGACY_BTN_COLOR = ('#f44e15','#f44e15', '#497ed6', '#497ed6', '#497ed6')
LEGACY_BTN_HL = ('#f49b7b', '#f49b7b', '#8ea7e6', '#8ea7e6', '#8ea7e6')

# Colors for the small buttons (Refresh / Log Out)
SMALLBTN_COLOR = 'white'
SMALLBTN_HL = 'white'

# Sizes and dimensions. The size of the overall window is set based on the
# smallest area everything can fit into. The defaults work for a 1280*1024 px
# screen with no window border, but you can adjust them as needed for your
# setup. Some tweaking is needed to find optimum values. Note that if your
# screen is too small, some will be cut off - it won't spawn a window too large
# for your monitor.

BTN_FONT = ("Helvetica", "22", "bold")			# Font for the buttons
BTN_HEIGHT = 3									# Height of a button, relative to font size
BTN_BORDER = 14									# Border width of the buttons
BTN_WRAPLENGTH = 200							# Wrap length for the button text

SMALLBTN_FONT = ("Helvetica", "16", "bold")		# Font for the buttons
REFRESH_WIDTH = 6								# Relative width of the Refresh button
LOGOUT_WIDTH = 7								# Relative width of the Log Out button
SMALLBTN_HEIGHT = 3								# Height of a button, relative to font size
SMALLBTN_BORDER = 14							# Border width of the buttons
SMALLBTN_WRAPLENGTH = 100						# Wrap length for the button text

# Texts for the Refresh and Log Out buttons
REFRESH = 'Refresh'
LOGOUT = 'Log Out'

# Cart layout. All of these settings define what a cart looks like and how the
# various elements are positioned. You may need to tweak them to find optimum
# values for your monitor.

# Width and height of a cart.
CART_WIDTH = 171
CART_HEIGHT = 168

# Define the polygons for the Stop and Play symbols.
STOP_X1 = 10
STOP_Y1 = 103
STOP_X2 = 48
STOP_Y2 = 141

PLAY_X1 = 10
PLAY_Y1 = 103
PLAY_X2 = 10
PLAY_Y2 = 141
PLAY_X3 = 48
PLAY_Y3 = 122

# Images for the "stop other", "submit audio ID" and "fire command" indicators.
STOPOTHER_IMAGE = 'stop.gif'
SUBMIT_IMAGE = 'submit.gif'
COMMAND_IMAGE = 'command.gif'

# Positions for the indicators. The images are anchored at the bottom-right.
STOPOTHER_X = 10
STOPOTHER_Y = 164

SUBMIT_X = 32
SUBMIT_Y = 164

COMMAND_X = 54
COMMAND_Y = 164

# Positions of the various texts. Captions are anchored at the top-left,
# and the timer is anchoredat the bottom-right
CAP1_X = 6
CAP1_Y = 4

CAP2_X = 6
CAP2_Y = 32

TIMER_X = 162
TIMER_Y = 140

# Fonts for the texts
CAP1_FONT = ("Helvetica", "16", "bold")
CAP2_FONT = ("Helvetica", "12")
TIMER_FONT = ("Helvetica", "42", "bold")

# Should the timer show minutes? If not, it'll just show the total seconds, even
# if that is greater than 60. Note that "zero minutes" is not displayed; and
# cart with less than one minute remaining is always just shown as seconds.
# The idea of cartwall is to play short clips, not songs or beds or other long
# pieces of audio; not showing a minutes field may might help your presenters
# to remember this!
SHOW_MINUTES = False

# This function is called whenever a "submit audio ID" function is played on a
# cart. Put whatever code you like here in order to process this submission.
# Typically you might build a URI of a script on your media management server
# and then call wget to fetch that URI, notifying the server that the audio
# has been played.
def submit_play(audio_id):
	pass

# This function is called whenever a "fire command" function is played on a
# cart. Put whatever code you like here in order to detect commands and process
# them. Typically you might build a URI of a script on your media management
# server and then call wget to fetch that URI, notifying the server that it
# should do something.
def run_command(cmd):
	pass





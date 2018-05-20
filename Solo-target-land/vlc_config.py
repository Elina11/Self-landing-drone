#!/usr/bin/env python2

import os

currDir = os.getcwd()

VLC_APP = "/Applications/VLC.app/Contents/MacOS/VLC" #Path to Mac VLC application
#SOLO_V_LINK = currDir + "../sololink.sdp"
SOLO_V_LINK = "/Users/elinasuslova/Desktop/GOPR5541.MP4"
SC_PATH = currDir + "/in_images"
SC_RATIO = "30"

VLC_START = VLC_APP + " " + SOLO_V_LINK + " --video-filter=scene" + " --scene-ratio=" + SC_RATIO + " --scene-path=" + SC_PATH + " vlc://quit"

#!/usr/bin/env python2

import os

currDir = os.getcwd()

# Path to Mac VLC application
VLC_APP = "/Applications/VLC.app/Contents/MacOS/VLC"

# DroneWifi streaming file
#SOLO_V_LINK = currDir + "/../sololink.sdp"

# Test Videos taking from flying Drone
#SOLO_V_LINK = currDir + "/../testVideos/TestVideo2.MP4"
#SOLO_V_LINK = currDir + "/../testVideos/TestVideo3.MP4"
SOLO_V_LINK = currDir + "/../testVideos/TestVideo4.MP4"

# Directory for Video screenshots
SC_PATH = currDir + "/in_images"

# Frames Ratio per screenshots
SC_RATIO = "30"

# VLC shell script command for Mac
VLC_START = VLC_APP + " " + SOLO_V_LINK + " --video-filter=scene" + " --scene-ratio=" + SC_RATIO + " --scene-path=" + SC_PATH + " vlc://quit"

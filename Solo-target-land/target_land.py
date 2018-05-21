#!/usr/bin/env python2

import os
import subprocess
import time
import signal
import vlc_config as VLC
import ai_image_analyzer as AImage

# Finds the latest screenshots.
# Returns most recent screen shot and command to delete files.
def newest(path):
    files = os.listdir(path)
    filtered_files = filter(lambda x: ".swp" not in x, files)
    paths = [os.path.join(path, basename) for basename in filtered_files]
    deleteThis = "rm -r " + deletefiles(paths)
    return max(paths, key=os.path.getctime), deleteThis

# List the screenshots to be deleted
def deletefiles(paths):
    picts = ""
    for x in range(0, len(paths)):
        picts = picts + " " + paths[x]
    return picts

# Kill running subprocess
def killAll(ncPro, vlcPro):
    if ncPro:
        os.killpg(os.getpgid(ncPro.pid), signal.SIGTERM)
    if vlcPro.poll() is None:
        os.killpg(os.getpgid(vlcPro.pid), signal.SIGTERM)

# Initialize Model
try:
    AiModel = AImage.ai_image_analyzer()
except Exception as e:
    print("Error Initializing Model: ", e)

# ncPro holds the process that opens connection port to the drone
ncPro = None
# vclPro holds the process for VLC player
vlcPro = None
# Init ncPro and vlcPro
if VLC.SOLO_V_LINK.endswith('.sdp'):
    ncPro = subprocess.Popen("nc 10.1.1.1 5502", shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
try:
    vlcPro = subprocess.Popen(VLC.VLC_START, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
except Exception as e:
    print("Error Initializing Video - Check your VLC config: ", e)
    killAll(ncPro, vlcPro)
    exit(1)

time.sleep(4)
x = 1
try:
    while vlcPro.poll() is None:

        sc_image, cleanFiles = newest(VLC.SC_PATH)

        print("File" + str(x) + "= " + sc_image)
        try:
            res = AiModel.isTarget(sc_image)
        except Exception as e:
            print("Model Error: ", e)
            res = None

        if res:
            print("File" + sc_image + "is: " + "target")
        else:
            print("File" + sc_image + "is: " + "not target")

        x += 1

        # Delete screenshots. Commented out for validation.
        subprocess.Popen(cleanFiles, shell=True, stdout=subprocess.PIPE)

        time.sleep(1)
except Exception as e:
    print("Unexpected error:", e)

killAll(ncPro, vlcPro)
exit(0)

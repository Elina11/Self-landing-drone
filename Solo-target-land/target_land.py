#!/usr/bin/env python2

import os
import subprocess
import time
import signal
import vlc_config as VLC
import ai_image_analyzer as AImage


def newest(path):
    files = os.listdir(path)
    filtered_files = filter(lambda x: ".swp" not in x, files)
    paths = [os.path.join(path, basename) for basename in filtered_files]
    deleteThis = "rm -r " + deletefiles(paths)
    return max(paths, key=os.path.getctime), deleteThis

def deletefiles(paths):
    picts = ""
    for x in range(0,len(paths)):
        picts = picts + " " + paths[x]
    return picts

AiModel = AImage.ai_image_analyzer()

vlcPro = subprocess.Popen(VLC.VLC_START, shell=True, stdout=subprocess.PIPE, preexec_fn=os.setsid)
time.sleep(2)
x=1
while(vlcPro.poll() == None):

    sc_image, cleanFiles = newest(VLC.SC_PATH)

    print("File" + str(x) + "= " + sc_image)

    res = AiModel.isTarget(sc_image)

    print("File" + sc_image + "is: " + res)

    x += 1
    subprocess.Popen(cleanFiles, shell=True, stdout=subprocess.PIPE)

    time.sleep(1)

if(vlcPro.poll() == None):
    os.killpg(os.getpgid(vlcPro.pid), signal.SIGTERM)
exit(1)


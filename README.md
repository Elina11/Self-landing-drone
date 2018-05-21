# Self-Landing-Drone
This project is a final project for SFSU CSC665 AI course. In this project we have build a CNN model which identifies if 
drone camera is detecting landing target during the flight. The idea of this project is to be able to identify if drone 
landing pad is present in the area of a flight and to perform a landing on available pad.

## Getting started 
In order to get started you will need to clone or download this repository. In order to run this project you will need 
to install jupyter notebook, keras, tensorflow, python2, matplotlib, itertools, sklearn, numpy, solo-cli, VLC video palyer.
For this project we have used Solo 3DR drone. Information about drone settings and configurations available at dev.3dr.com 


## How to run it
In order to run this project make sure that you are connected to Solo 3DR  wireless network. 
Check if drone camera is on and ready to record a video.
Open a terminal and navigate to Solo-target-land directory. 
From terminal execute a command: "python target_land.py"
This will start vlc video player which will display a video from a drone camera, as well as program will get frames from 
the video and feed it to the model, where it will identify if current frame contains target or not, and the prediction will 
be displayed in the terminal.

## Sample
It is possible to test this project without flying the drone.
In order to do it open vlc_config.py file located in Solo-target-land folder and comment out following line: 
SOLO_V_LINK = currDir + "/../sololink.sdp"
Then add path to a video you would like to test this model on  in the following format:
SOLO_V_LINK = "path_to_the_video"
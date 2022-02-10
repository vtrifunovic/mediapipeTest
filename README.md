# mediapipeTest
Different CVIP programs based around around mediapipe's hand tracking

# Main required dependencies
- mediapipe
- opencv-python

# Description of programs in folder:
# Handtracking module
Contains the handtracking class, which initializes all the data that will be tracked/used in the rest of the projects.
Running solo will simply display the handtracking module and plot where the tip of the index is on the camera (in pixels)

# volumehandcontrol
Additional required dependecnies for this file:
- numpy
- comtypes
- pycaw

File will interpolate the distance between the index and thumb and adjust the computer's volume based off of the distance

# csgoplayer
Additional required dependecnies for this file:
- keyboard
- numpy
- autopy

File runs two sepearate threads, one which focuses on the left half of the camera, and uses the position of the index finger's tip to determine what "key" is being pressed.
This send a continuous input of the selected key till the index finger is moved out of the "key" region.
Second thread focuses on the right half of the camera, it uses the position of the index finger relative to the camera to determine where to move the mouse. 
Only index finger up will result in simple mouse tracking, index and middle finger up will count as a "click" or press of mouse 1.

IMPORTANT NOTE: this program is not VAC safe, nor has it been tested against VAC, use this only with friends in LAN/Private games. I am not responsible for any bans resulting from this program.

# measure
Additional required dependecnies for this file:
- numpy

This file is meant to look for two blue X's on a piece of paper, and interpolate this distance to inches.
This is done to determine the hand's position from the topleft most X. Program was used to measure the depth of chest compressions during CPR training.

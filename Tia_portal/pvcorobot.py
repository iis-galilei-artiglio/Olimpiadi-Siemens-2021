!/usr/bin/python3

# PVCorobot AI
#

import jetson.inference
import jetson.utils

import argparse
import sys

import numpy as np
import cv2

import matplotlib.pyplot as plt

import socket
import os
from time import sleep

HOST, PORT = "192.168.1.2", 2000 # PLC address

send = ''

def plcnt(data):
   with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
       s.settimeout(1)   # 1 seconds

       try:
           s.connect((HOST, PORT))
           print('Connecting to server ..')
           print('Connected to', s.getsockname())

           # send
           send = data
           s.sendall(send.encode())
           print('\n\nCOMPLETED!\n')
           s.close()

       except socket.error as msg:
           s = None
           print('Caught exception socket.error:')
           print(msg)

   #s.close()


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
camera = jetson.utils.videoSource("/dev/video0")      # '/dev/video0' for V4L2
display = jetson.utils.videoOutput("display://0") # 'my_video.mp4' for file


while display.IsStreaming():
	img = camera.Capture()
	detections = net.Detect(img)
	display.Render(img)
	display.SetStatus("Object Detection | Network {:.0f} FPS".format(net.GetNetworkFPS()))
	print("detected {:d} objects in image".format(len(detections)))

	if len(detections) == 0 :
		coord='-----------'
		sleep(0.01)
		plcnt(coord)
	else :

	   for detection in detections:
	     idt = (detection.ClassID)
	     bx, by = (detection.Center) # spacchettamento della tupla
	     area = (detection.Area)
	     coord=(str(int(idt))+'-'+str(int(bx/10))+'-'+str(int(by/10))+'-'+str(int(area/100))) # costruzione stringa di interi
	     sleep(0.01)
	     #print(int(bx/10))
	     plcnt(coord)

#!/usr/bin/env python3

# install ffmpeg first
# sudo apt-get install libzbar0
# pip3 install pyzbar opencv-python
# python video_qrcode_cut.py -i test2.mp4 -o out.mp4

import cv2
from pyzbar import pyzbar

import argparse
import os
import sys

SPAN_MIN=10
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input_mp4", required=True,help="Path to mp4 video to cut")
ap.add_argument("-o", "--output_mp4", required=True,help="Path to output")
args = ap.parse_args()

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "%d:%02d:%02d" % (hour, minutes, seconds)


# initalize the cam
cap = cv2.VideoCapture(args.input_mp4)
# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
frame_count = frame_count - fps
frame_number = 0
success=True
start=-1
end=-1
while success and frame_number<=frame_count:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    success, img = cap.read()
    print(frame_number)
    if img is None:
        print(frame_number,'img none')
        if start == -1:
            frame_number += fps
        else:
            #reverse searching
            frame_number -= fps
        continue
    # detect and decode
    result=pyzbar.decode(img)
    if not result:
        print(frame_number,'result none',result)
        if start == -1:
            frame_number += fps
        else:
            #reverse searching
            frame_number -= fps
        continue
    result = result[0]
    data = result.data.decode("utf-8")
    data_type = result.type

    if data=='bot5.club/start':
        print("QR Code detected, start data:",data ,frame_number)
    elif data=='bot5.club/end':
        print("QR Code detected, end data:",data ,frame_number)
    else:
        print("QR Code detected, dummy data:",data ,frame_number)

    if start ==-1 and data=='bot5.club/start':
        start=frame_number
        print(start,data)
        #reverse search end for long video
        frame_number=frame_count-1
    elif end == -1 and data=='bot5.club/end':
        print("QR Code detected, raw data:",data ,frame_number)
        end=frame_number
        break
    else:
        if start == -1:
            frame_number += fps
        else:
            #reverse searching
            frame_number -= fps

cap.release()
if start<0 or end <0:
    print('err: not found.start:%d,end:%d'%(start,end))
    sys.exit()
span=(end-start)/fps
span_human=convert(span)
start_human=convert(start/fps)
end_human=convert(end/fps)
print(start_human,end_human,span_human)
cmd = "ffmpeg -i '%s' -ss %s -t %s -c copy '%s'"%(args.input_mp4,start_human,span_human,args.output_mp4)
print(cmd)
if span > SPAN_MIN:
    os.system(cmd)

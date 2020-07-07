#!/usr/bin/env bash

START_TIME=$1
DURATION_TIME=$2

ffmpeg -ss "$START_TIME" -t "$DURATION_TIME" -i zoom.mp4 -map 0 -c copy out.mp4

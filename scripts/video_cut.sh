#!/usr/bin/env bash

START_TIME=$1
DURATION_TIME=$2
INPUT_FILE=$3
OUTPUT_FILE=$4

ffmpeg -ss "$START_TIME" -t "$DURATION_TIME" -i "$INPUT_FILE" -map 0 -c copy "$OUTPUT_FILE"

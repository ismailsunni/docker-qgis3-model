#!/bin/bash

echo "Start Script"
# xvfb-run -e $XVFB_LOGFILE python3 /code/main.py /data/output/clipped_raster.tif
# Get input from the first argument, a path to tif file and the output
xvfb-run -e $XVFB_LOGFILE python3 /code/main.py $1 $2

echo "XVFB LOGFILE"
cat $XVFB_LOGFILE

echo "Finish script"
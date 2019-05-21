#!/bin/bash

echo "Start Script"
xvfb-run -e $XVFB_LOGFILE python3 /code/run.py

echo "XVFB LOGFILE"
cat $XVFB_LOGFILE

echo "Finish script"
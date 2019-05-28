#!/bin/bash

echo "Start Script"
xvfb-run -e $XVFB_LOGFILE python3 /code/main.py /data/test_data/routing-docker.yaml

echo "XVFB LOGFILE"
cat $XVFB_LOGFILE

echo "Finish script"
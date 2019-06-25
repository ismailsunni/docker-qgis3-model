FROM qgis/qgis

LABEL maintainer="Ismail Sunni<imajimatika@gmail.com>"

# Install needed package
RUN apt-get update && apt-get install -qqy --no-install-recommends \
    xvfb

# Enviroment variables
ENV XVFB_LOGFILE=/qgis/xvfb.log

# Prepare directories for code
RUN mkdir /code
WORKDIR /code

# Prepare directories for data
RUN mkdir /data
RUN mkdir /data/input
RUN mkdir /data/output
RUN mkdir /data/tmp

# Prepare direcotry for QGIS
RUN mkdir /qgis

# Copy needed files
# Function to run the algorithm
COPY algorithm_runner.py /code/algorithm_runner.py
# Main python file to handle the input
COPY main.py /code/main.py
# Provider for the algorithm
COPY ndvi_provider.py /code/ndvi_provider.py
# Algorithm to split the band
COPY split_band.py /code/split_band.py
# Algorithm to calculate NDVI
COPY ndvi_raster_calculator.py /code/ndvi_raster_calculator.py
# Entry point to run the code with xfvb
COPY start.sh /code/start.sh

# Entry point
# ENTRYPOINT [ "/bin/bash" ]

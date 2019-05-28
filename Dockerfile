FROM qgis/qgis

LABEL maintainer="Ismail Sunni<imajimatika@gmail.com>"

# Install needed package
RUN apt-get update && apt-get install -qqy --no-install-recommends \
    xvfb

# Enviroment variables
ENV XVFB_LOGFILE=/qgis/xvfb.log

# Prepare directories
RUN mkdir /qgis
RUN mkdir /code
WORKDIR /code

RUN mkdir /data

# Copy needed files
COPY algorithm_runner.py /code/algorithm_runner.py
COPY main.py /code/main.py
COPY start.sh /code/start.sh

# Entry point
# ENTRYPOINT [ "/bin/bash" ]

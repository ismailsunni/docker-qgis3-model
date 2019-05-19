FROM qgis/qgis

LABEL maintainer="Ismail Sunni<imajimatika@gmail.com>"

# Prepare directories
RUN mkdir /code
WORKDIR /code

# Copy needed files
COPY run.py /code/run.py

# Entry point
CMD [ "python3", "/code/run.py" ]

# docker-qgis3-model

Docker image for running QGIS 3 model.

Is it working? Yes. Proof of concept with calculating NDVI as example.

How to run it locally:

1. Clone the repo locally `git clone https://github.com/ismailsunni/docker-qgis3-model.git`
2. Build the docker image: `make build-qgis3-model`
3. Run example: `make run-qgis3-model`

## Notes

1. I can't load QGIS 3 processing model directly from the file. So, I need to convert the model to python script (you can do it in one click from QGIS 3), then add it to the `provider` class.
2. My ideal plan would be: making it very dynamic so that it can take QGIS processing model files, data, and the parameter (to run the model) as an input then give the result in the output directory

## References

Here are some source that I use for reference and inspiration:

1. [Run QGIS Desktop with Docker - Kartoza](]https://github.com/kartoza/docker-qgis-desktop)
2. [Run QGIS model with Docker, but it is QGIS 2 - Daniel Nuest](https://github.com/nuest/docker-qgis-model)
3. [Another run QGIS model with Docker, but it is using QGIS 2 - Sebastian Holtkamp](https://github.com/sholtkamp/Bachelorarbeit)

## "Similar" Works

1. [QGIS QEP - QGIS Processing standalone executable](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/140)

@ismailsunni - 2019

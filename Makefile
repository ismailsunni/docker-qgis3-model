build-qgis3-model:
	docker build -t ismailsunni/qgis3-model .

run-qgis3-model:
	docker run -it --rm ismailsunni/qgis3-model

shell-qgis3-model:
	docker run -it --rm ismailsunni/qgis3-model /bin/bash

python-qgis3-model:
	docker run -it --rm ismailsunni/qgis3-model python3

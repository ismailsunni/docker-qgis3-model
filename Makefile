build-qgis3-model:
	docker build -t ismailsunni/qgis3-model .

shell-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model /bin/bash

python-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model python3

run-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data/input:/data/input -v ${PWD}/data/output:/data/output  ismailsunni/qgis3-model /bin/bash start.sh 'clipped_raster.tif' 'ndvi.tif'

run-qgis3-model-real:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data/input:/data/input -v ${PWD}/data/output:/data/output  ismailsunni/qgis3-model /bin/bash start.sh "Orthophoto_MAPIR.tif" "ndvi-mapir.tif"

remove-output:
	rm -rf ./data/output
	git checkout ./data/output

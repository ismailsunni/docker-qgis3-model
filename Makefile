build-qgis3-model:
	docker build -t ismailsunni/qgis3-model .

run-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model /bin/bash start.sh

shell-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model /bin/bash

python-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model python3

new-run-qgis3-model:
	docker run --name test_qgis3_model -it --rm -v ${PWD}/data:/data  ismailsunni/qgis3-model /bin/bash start.sh 'input' 'output'
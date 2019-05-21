import sys
import qgis.utils

from qgis.core import (
     QgsApplication, 
     QgsProcessingFeedback, 
     QgsVectorLayer
)
from qgis.analysis import QgsNativeAlgorithms

# See https://gis.stackexchange.com/a/155852/4972 for details about the prefix 
QgsApplication.setPrefixPath('/usr', True)
qgs = QgsApplication([], False)
qgs.initQgis()

#  # Append the path where processing plugin can be found
sys.path.append('/usr/share/qgis/python/plugins/')

import processing
from processing.core.Processing import Processing
Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())

print('Hello world')
print('You are using QGIS version ' + qgis.utils.Qgis.QGIS_VERSION)
print(QgsApplication.processingRegistry().algorithms())

algorithm_id = 'qgis:addfieldtoattributestable'
algorithm_parameter = {
    'INPUT': '/data/test_data/routing.geojson',
    'FIELD_NAME': 'new_field',
    'FIELD_TYPE': 0,
    'FIELD_LENGTH': 10,
    'FIELD_PRECISION': 0,
    'OUTPUT': '/data/test_data/added_routing.geojson',
    }

processing.algorithmHelp(algorithm_id)
print('Running algorithm')
result = processing.run(algorithm_id, algorithm_parameter)
print('The result is in ' + result['OUTPUT'])

# qgis:addfieldtoattributestable

qgs.exitQgis()

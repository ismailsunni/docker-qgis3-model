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

qgs.exitQgis()

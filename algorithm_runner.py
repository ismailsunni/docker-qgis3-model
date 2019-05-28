# Module to run QGIS algorithm

from ndvi import Calculate_ndvi
from ndvi_provider import NDVIProvider

def run_qgis_algorithm(algorithm_id, algorithm_parameters):
    import sys
    import qgis.utils

    from qgis.core import (
        QgsApplication, 
        QgsProcessingFeedback, 
        QgsVectorLayer,
        QgsProcessingProvider,
        QgsProcessingRegistry,
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

    print('You are using QGIS version ' + qgis.utils.Qgis.QGIS_VERSION)
    previous_algs = QgsApplication.processingRegistry().algorithms()
    previous_num = len(QgsApplication.processingRegistry().algorithms())
    print('Number of algorithm: ' + str(previous_num))

    # algorithm_id = 'qgis:addfieldtoattributestable'
    # algorithm_parameters = {
    #     'INPUT': '/data/test_data/routing.geojson',
    #     'FIELD_NAME': 'new_field',
    #     'FIELD_TYPE': 0,
    #     'FIELD_LENGTH': 10,
    #     'FIELD_PRECISION': 0,
    #     'OUTPUT': '/data/test_data/added_routing.geojson',
    #     }

    # Show help for the algorithm
    # processing.algorithmHelp(algorithm_id)
    print('Running algorithm')
    # result = processing.run(algorithm_id, algorithm_parameters)
    # print('The result is in ' + result['OUTPUT'])

    # c = Calculate_ndvi().createInstance()
    c = NDVIProvider()
    c.loadAlgorithms()
    QgsApplication.processingRegistry().addProvider(c)
    now_algs = QgsApplication.processingRegistry().algorithms()
    now_num = len(QgsApplication.processingRegistry().algorithms())
    print('Previous number' + str(previous_num))
    print('Now number' + str(now_num))
    last_alg = QgsApplication.processingRegistry().algorithms()[-1]
    print(last_alg.name())
    print(last_alg.id())

    qgs.exitQgis()
    # return result['OUTPUT']
    return ''

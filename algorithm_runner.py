# Module to run QGIS algorithm

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

    print('You are using QGIS version: %s ', qgis.utils.Qgis.QGIS_VERSION)
    print('You are running:  %s ', algorithm_id)

    provider = NDVIProvider()
    provider.loadAlgorithms()

    QgsApplication.processingRegistry().addProvider(provider)
    
    # Checking if the algorithm is added
    # last_alg = QgsApplication.processingRegistry().algorithms()[-1]
    # print(last_alg.name())
    # print(last_alg.id())
    # last_alg = QgsApplication.processingRegistry().algorithms()[-2]
    # print(last_alg.name())
    # print(last_alg.id())

    # Show help for the algorithm
    processing.algorithmHelp(algorithm_id)
    print('Running algorithm')
    result = processing.run(algorithm_id, algorithm_parameters)
    print('### Result:')
    print(result)

    qgs.exitQgis()
    return result

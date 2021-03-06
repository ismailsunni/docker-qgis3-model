# Main python file to run

import argparse
import yaml
import os
import sys

# from algorithm_runner import run_qgis_algorithm
from ndvi_provider import NDVIProvider

# default directory in docker
INPUT_DIRECTORY = '/data/input'
TEMP_DIRECTORY = '/data/tmp'
OUTPUT_DIRECTORY = '/data/output'

def main_function(tif_file_name, output_file_name, input_directory=INPUT_DIRECTORY, output_directory=OUTPUT_DIRECTORY):
    """The main function to calculate NDVI from tif file in `tif_path` to `output_path`
    """
    full_tif_path = os.path.join(input_directory, tif_file_name)
    full_output_path = os.path.join(output_directory, output_file_name)
    if not os.path.exists(full_tif_path):
        print('TIF file %s is not exist' % full_tif_path)
    else:
        print('TIF file %s is exist' % full_tif_path)

    #### Prepare QGIS ####
    import sys
    import qgis.utils

    from qgis.core import (
        QgsApplication, 
        QgsProcessingFeedback, 
        QgsVectorLayer,
        QgsProcessingProvider,
        QgsProcessingRegistry,
        QgsRasterLayer,
        QgsProject
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

    #### Add NDVI Provider ####
    provider = NDVIProvider()
    provider.loadAlgorithms()

    QgsApplication.processingRegistry().addProvider(provider)
    
    #### Run split bands algorithm ####
    # algorithm id: 
    split_band_algorithm_id = 'uas:Split_bands'
    # parameters
    split_band_algorithm_parameters = {
        'inputimage': full_tif_path,
        'Red': os.path.join(TEMP_DIRECTORY, 'red.sdat'),
        'Green': os.path.join(TEMP_DIRECTORY, 'green.sdat'),
        'Blue': os.path.join(TEMP_DIRECTORY, 'nir.sdat'),
        'R_conv': os.path.join(OUTPUT_DIRECTORY, 'red_conv.tif'),
        'G_conv': os.path.join(OUTPUT_DIRECTORY, 'green_conv.tif'),
        'B_conv': os.path.join(OUTPUT_DIRECTORY, 'nir_conv.tif'),
    }
    # Run algorithm
    split_band_result = processing.run(split_band_algorithm_id, split_band_algorithm_parameters)

    # Check result
    print('Path of G_conv: %s is exist = %s' % (split_band_result.get('G_conv'), os.path.exists(split_band_result.get('G_conv'))))
    print('Path of R_conv: %s is exist = %s' % (split_band_result.get('R_conv'), os.path.exists(split_band_result.get('R_conv'))))

    
    #### Run NDVI raster calculation algorithm ####
    # algorithm id: 
    ndvi_algorithm_id = 'uas:Calculate_NDVI'
    # parameters
    ndvi_algorithm_parameters = {
        'inputnirband': split_band_result['B_conv'],
        'inputredband': split_band_result['R_conv'],
        'Output': full_output_path
    }
    if False:
        # Run algorithm
        ndvi_result = processing.run(ndvi_algorithm_id, ndvi_algorithm_parameters)

        # Check result
        print('Path of NDVI: %s is exist = %s' % (ndvi_result.get('Output'), os.path.exists(ndvi_result.get('Output'))))
    else:
        from qgis.analysis import QgsRasterCalculator, QgsRasterCalculatorEntry
        
        entries = []

        nir_layer = QgsRasterLayer(ndvi_algorithm_parameters['inputnirband'], "nir")
        QgsProject.instance().addMapLayer(nir_layer)
        nir = QgsRasterCalculatorEntry()
        nir.ref = 'nir@1'
        nir.raster = nir_layer
        nir.bandNumber = 1
        entries.append(nir)

        red_layer = QgsRasterLayer(ndvi_algorithm_parameters['inputredband'], "red")
        QgsProject.instance().addMapLayer(red_layer)
        red = QgsRasterCalculatorEntry()
        red.ref = 'red@1'
        red.raster = red_layer
        red.bandNumber = 1
        entries.append(red)

        ndvi_expression = 'Float( nir@1 - red@1 ) / Float( nir@1 + red@1 )'

        calc = QgsRasterCalculator(
            ndvi_expression, ndvi_algorithm_parameters['Output'], 'GTiff', nir_layer.extent(), nir_layer.width(), nir_layer.height(), entries)
        
        a = calc.processCalculation()
        print('Result: ', a)

    # Exit QGIS
    qgs.exitQgis()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tif_file_name", help="TIF input file name")
    parser.add_argument("output_file_name", help="Output file name")
    args = parser.parse_args()
    tif_path = args.tif_file_name
    print('Input TIF file name: %s' % args.tif_file_name)
    print('Output path: %s' % args.output_file_name)
    main_function(args.tif_file_name, args.output_file_name)
    print('fin')

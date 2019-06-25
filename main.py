# Main python file to run

import argparse
import yaml
import os
import sys

from algorithm_runner import run_qgis_algorithm

# default directory in docker
INPUT_DIRECTORY = '/data/input'
TEMP_DIRECTORY = '/data/tmp'

def main_function(tif_path, output_path, input_directory=INPUT_DIRECTORY):
    """The main function to calculate NDVI from tif file in `tif_path` to `output_path`
    """
    full_tif_path = os.path.join(input_directory, tif_path)
    if not os.path.exists(full_tif_path):
        print('TIF file %s is not exist' % full_tif_path)
    else:
        print('TIF file %s is exist' % full_tif_path)
    
    # Run split bands algorithm
    # algorithm id: 
    split_band_algorithm_id = 'uas:Calculate_NDVI2'
    # parameters
    split_band_algorithm_parameters = {
        'inputimage': full_tif_path,
        'Red': os.path.join(TEMP_DIRECTORY, 'red.sdat'),
        'Green': os.path.join(TEMP_DIRECTORY, 'green.sdat'),
        'Blue': os.path.join(TEMP_DIRECTORY, 'blue.sdat'),
        'G_conv': os.path.join(TEMP_DIRECTORY, 'g_conv.tiff'),
        'R_conv': os.path.join(TEMP_DIRECTORY, 'r_conv.tiff'),
    }
    # Run algorithm
    result = run_qgis_algorithm(split_band_algorithm_id, split_band_algorithm_parameters)

    # Check result
    print('Path of G_conv: %s is exist = %s' % (result.get('G_conv'), os.path.exists(result.get('G_conv'))))
    print('Path of R_conv: %s is exist = %s' % (result.get('R_conv'), os.path.exists(result.get('R_conv'))))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tif_file_name", help="TIF input file name")
    parser.add_argument("output_file_name", help="Output file name")
    args = parser.parse_args()
    tif_path = args.tif_file_name
    print('Input TIF file name: %s' % args.tif_file_name)
    print('Output path: %s' % args.output_file_name)
    main_function(args.tif_file_name, args.output_file_name)
    # if not os.path.exists(yaml_path):
    #     print('File not found at ' + yaml_path)
    #     sys.exit()
    # with open(yaml_path, 'r') as stream:
    #     try:
    #         configuration = yaml.safe_load(stream)
    #         print('Algorithm ID: ' + configuration['algorithm_id'])
    #         print('Algorithm parameter: ')
    #         for k, v in configuration['algorithm_parameters'].items():
    #             print(k + ' : ' + str(v))
    #     except FileNotFoundError:
    #         print('File not found at ' + yaml_path)
    #     except yaml.YAMLError as exc:
    #         print(exc)
    # print('run algorithm')
    # run_qgis_algorithm(configuration['algorithm_id'], configuration['algorithm_parameters'])
    print('fin')

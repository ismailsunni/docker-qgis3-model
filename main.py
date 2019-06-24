# Main python file to run

import argparse
import yaml
import os
import sys

from algorithm_runner import run_qgis_algorithm

def main_function(tif_path, output_path):
    """The main function to calculate NDVI from tif file in `tif_path` to `output_path`
    """
    if not os.path.exists(tif_path):
        print('TIF file %s is not exist' % tif_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("tif", help="TIF input")
    parser.add_argument("output", help="Output path")
    args = parser.parse_args()
    tif_path = args.tif
    print('Input TIF: %s' % args.tif)
    print('Output path: %s' % args.output)
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

import argparse
import yaml
import os

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("yaml", help="YAML Configuration Path")
    args = parser.parse_args()
    yaml_path = args.yaml
    print(yaml_path)
    print(os.path.exists(yaml_path))
    with open(yaml_path, 'r') as stream:
        try:
            configuration = yaml.safe_load(stream)
            print('Algorithm ID: ' + configuration['algorithm_id'])
            print('Algorithm parameter: ')
            for k, v in configuration['parameters'].items():
                print(k + ' : ' + str(v))
        except yaml.YAMLError as exc:
            print(exc)
    print('fin')
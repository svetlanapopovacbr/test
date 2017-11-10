import argparse
import os.path
import yaml

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--config', dest='config', action='store', type=str, #-с и --config - same shit
        help='path to custom config',
        default=os.path.join(os.path.dirname(__file__), "config.yaml")
    )
    return parser

def load_config(filepath):
	with open(filepath, "r") as cfgfile:
		conf = yaml.load(cfgfile.read())
	return conf

def main():
    parser = build_parser()
    params, other_params = parser.parse_known_args()
    conf = load_config(params.config)
    print(conf)

if __name__== "__main__":
 	main()
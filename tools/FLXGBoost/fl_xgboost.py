''' DT4H Site Status. Obtain full technical status of DT4H sites
'''
import argparse
import json

parser = argparse.ArgumentParser(
    prog="site_status",
    description="retrieve status of a site"
)

parser.add_argument('--config', type=open, help="DT4H configuration", required=True)
parser.add_argument('--param', type=open, help="Analysis parameters", required=True)
parser.add_argument('--datasets', help="DT4H datasets")
parser.add_argument('--manifest', help="DT4H datasets manifest")
parser.add_argument('--output_path', action='store', help="Output file", required=True)

args = parser.parse_args()

config = json.load(args.config)

#TODO
with open(args.output_path, "w") as output_file:
    json.dump(config, output_file)

''' EUCAIM Site Status. Obtain full technical status of EUCAIM sites
'''
import argparse
import json

parser = argparse.ArgumentParser(
    prog="site_status",
    description="retrieve status of a site"
)

parser.add_argument('--config', type=open, help="EUCAIM configuration", required=True)
parser.add_argument('--output_path', action='store', help="Output file", required=True)

args = parser.parse_args()

config = json.load(args.config)

#TODO
with open(args.output_path, "w") as output_file:
    json.dump(config, output_file)

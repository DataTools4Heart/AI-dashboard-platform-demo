''' DT4H Site Status. Obtain full technical status of a given site
'''
import argparse
import json

parser = argparse.ArgumentParser(
    prog="site_status",
    description="retrieve status of a site"
)

parser.add_argument('--config', type=open, help="DT4H configuration")
parser.add_argument('site_id', help='Id of site')

args = parser.parse_args()

config = json.load(args.config)

#TODO

print(json.dumps(config))

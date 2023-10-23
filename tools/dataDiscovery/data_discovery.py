''' Site Status. Obtain full technical status of project sites
'''
import argparse
import json
import random

parser = argparse.ArgumentParser(
    prog="data_discovery",
    description="retrieve materialized datasets"
)
PROJECT = 'EUCAIM'
FAKE_IDS = ['100299', '100300', '100304','100305','100301']
MAX_DTS = 3

parser.add_argument('--config', type=open, help="Project configuration", required=True)
parser.add_argument('--sites', action='store', help="Available sites", required=True)
parser.add_argument('--output_path', action='store', help="Output file", required=True)

args = parser.parse_args()

config = json.load(args.config)

datasets = []

for site in args.sites.split(","):
    dts = set()
    data = {
        'site': site,
        'datasets': []
    }
    i = 0
    while i < MAX_DTS:
        rnd_id = PROJECT + FAKE_IDS[random.randint(0, len(FAKE_IDS)-1)]
        if rnd_id not in dts:
            data['datasets'].append({
                'id': rnd_id,
                'local_path': f"/userdata/{rnd_id}",
                'metadata' : {
                    'count': random.randint(10, 100),
                    'other_metadata': {}
                }
            })
            dts.add(rnd_id)
            i += 1
    datasets.append(data)

with open(args.output_path, "w") as output_file:
    json.dump(datasets, output_file, indent=4)


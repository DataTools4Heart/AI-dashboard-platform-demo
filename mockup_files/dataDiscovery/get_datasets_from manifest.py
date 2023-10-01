import json
import sys

with open (sys.argv[1], 'r') as manifest_file:
    data = json.load(manifest_file)
    for item in data:
        for dts in item['datasets']:
            new_ref = item['site'] + ":" + dts['id']
            dts['site'] = item['site']
            with open(new_ref + ".json", "w") as dataset_file:
                json.dump(dts, dataset_file, dts, indent=4, sort_keys=True)

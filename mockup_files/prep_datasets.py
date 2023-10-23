import sys
import json
import os
import random

PROJECT_PREFIX = "EUCAIM"

#Progress
PENDING = 0
TESTING = 1
ACTIVE = 2
#Status
DOWN = 0
UP = 1

class Site():
    """ Base class for sites"""
    def __init__(self, id, name, type):
        self_id = id
        self.data = {
            '_id': id,
            'name': name,
            'type': type,
            'status': 0,
            'progress': 0,
            'cpu_count': 0,
            'cpu_percent': 0,
            'gpu_count': 0,
            'memory': {
                'available': 0,
                'total': 0
            },
            'outbound_connectivity': False,
            'inbound_ports_connectivity': False
        }
        if self.data['type'] == 'comp':
            self.data['outbound_connectivity'] = True
            self.data['inbound_ports_connectivity'] = [80, 443]
        self.data['progress'] = random.randint(0, 2)
        if self.data['progress'] == 2:
            self.data['cpu_count'] = random.randrange(4)
            self.data['cpu_percent'] = random.uniform(10,90)
            self.data['memory']['total'] = random.randrange(48)
            self.data['memory']['available'] = random.uniform(0, self.data['memory']['total'])
            self.data['status'] = random.randint(0, 1)

class Dataset():
    def __init__(self, id, site, path):
        self._id = id
        self.data = {
            '_id': id,
            'site': site,
            'path': path,
            'metadata': {}
        }


class Manifest():
    """ Base class for data and site manifest"""
    def __init__(self, id):
        self._id = id
        self.items = []

    def append(self, site):
        self.items.append(site)

    def prep_item(self, item):
        continue

    def to_json(self, to_print=True):
        to_print_data = []
        for site in self.sites:
            to_print_data.append(site.data)
        json_data = json.dumps(to_print_data, indent=4)

        if to_print:
            with open(f"{self._id}.json", "w") as json_file:
                json_file.write(json_data)
        else:
            return json_data

class SiteManifest(Manifest):
    """ Base class for site manifest"""

    def to_json(self, to_print=True):
        to_print_data = []
        for site in self.sites:
            to_print_data.append(site.data)
        json_data = json.dumps(to_print_data, indent=4)

        if to_print:
            with open(f"{self._id}.json", "w") as json_file:
                json_file.write(json_data)
        else:
            return json_data




# EUCAIM
# siteDiscovery
DIR = 'siteDiscovery'

if not os.path.isdir(DIR):
    os.mkdir(DIR)

sites = Manifest(f"{DIR}/{PROJECT_PREFIX}_sites_report")
with open (sys.argv[1], 'r') as sites_file:
    for line in sites_file:
        _id, name, site_type = line.strip().split(',')
        sites.append(Site(_id, name, site_type))

sites.to_json()

# dataDiscovery
for site in sites:
    if site.data['status']=
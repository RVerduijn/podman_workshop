#!/usr/bin/env python
import os
import sys
import argparse

try:
    import json
except ImportError:
    import simplejson as json

number_of_workstations = os.getenv('WORKSTATIONS', '2')
domain = os.getenv('DOMAIN', 'qstars.lab')

class ExampleInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.example_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory))

    # Example inventory for testing.
    def example_inventory(self):
        inventory={
            'workstations': { 'hosts': [], 'vars': {} },
            'ipaclients': { 'hosts': [], 'vars': {} },
            '_meta': { 'hostvars': {} }}
        for host in range(1,int(number_of_workstations)+1):
            workstation='workstation' + str(host + 10) + '.' + domain
            ipaddress='10.10.1.' + str(host + 10)
            for group in ['ipaclients', 'workstations']:
                inventory[group]['hosts'].append(workstation)
            inventory['_meta']['hostvars'][workstation]={
                    'ansible_host': ipaddress,
                    'ansible_user': 'student',
                    'network_connections':
                    [
                        { 
                        'name': 'eth0', 'state': 'up', 'type': 'ethernet',
                        'interface_name': 'eth0', 'ip': {
                            'address': [ ipaddress + '/24'],
                            'dns': ['10.10.1.10'], 'dns_search': [domain], 'gateway4': '10.10.1.1'
                            },
                        },
                        { 'name': 'ens3', 'state': 'absent' },
                        { 'name': 'System eth0', 'state': 'absent' }
                    ]
                }
        return inventory

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()

# Get the inventory.
ExampleInventory()

    
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# (c) 2019 Jacob Salmela <me@jacobsalmela.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = """
short_description: A dynamic inventory script that uses the Spacewalk API
description:
    - A dynamic inventory script for Ansible
version_added: "2.8"
options:
# One or more of the following
    option_name:
        description:
            - Description of the options goes here.
            - Must be written in sentences.
        required: true or false
        default: a string or the word null
        choices:
          - enable
          - disable
        aliases:
          - repo_name
        version_added: "2.8"
requirements:
    - Click == 7.0
"""

# This file is part of Ansible.
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

# notes:
# Tested on Ansible v2.9.21
# This is a dynamic inventory script 

import json
import sys
import os
import argparse

number_of_workstations = os.getenv('WORKSTATIONS', '2')
domain = os.getenv('DOMAIN', '2')

# dynamic_inventory = { "group": { "hosts": [], "vars": {} }, "_meta": {} } }
dynamic_inventory = {}
dynamic_inventory["workstations"] = { "hosts": [], "vars": {}, "_meta": {} }


def gen_inventory():
    """Generate hosts and groups and vars"""
    for workstation in range(number_of_workstations + 10):
      dynamic_inventory["workstations"]["hosts"].append('workstation' + workstation + '.' + domain)
    inventory = json.dumps(dynamic_inventory)
    print(inventory)

def workstation_inventory():
    """A dynamic inventory script for Ansible"""
    pass


if __name__ == '__main__':
    workstation_inventory()
    
import codecs
import csv
import os

import requests
from django.core.management.base import BaseCommand

from nodes.models import Node


URL = 'https://www.mcs.anl.gov/research/projects/waggle/downloads/beehive1/nodes.csv'


class Command(BaseCommand):
    help = 'Seeds node data from the live nodes dump found in the MCS archives'

    def handle(self, *args, **options):
        known_nodes = set(Node.objects.values_list('id', flat=True))

        res = requests.get(URL)
        res.raise_for_status()

        reader = csv.DictReader(codecs.iterdecode(res.iter_lines(), 'utf-8'))
        for row in reader:
            if row['node_id'] not in known_nodes:
                self.stdout.write(f'Adding node {row["node_id"]}')
                
                vsn = row['vsn']
                location = row['location']
                description = row['description']

                if '(T)' in description or 'Returned' in location or 'RET' in vsn:
                    state = 'decommissioned'
                elif 'Surya Burn-In' in location:
                    state = 'burn in'
                elif '!' in vsn:
                    state = 'testing'
                elif vsn is not None:
                    state = 'deployed'
                else:
                    state = 'build out' 
                
                Node(
                    id=row['node_id'],
                    name=vsn,
                    ssh_port=row['reverse_ssh_port'],
                    address=location,
                    description=description,
                    state=state
                ).save()

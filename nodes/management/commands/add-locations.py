import codecs
import csv
import os
import shutil
from datetime import date

import requests
from django.core.management.base import BaseCommand

from nodes.models import Node


class Command(BaseCommand):
    help = 'Adds lat-lon pairs to nodes from the metadata archives'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        tarball_name = options['url'].split('/')[-1]
        
        with requests.get(options['url'], stream=True) as res:
            with open(tarball_name, 'wb') as fh:
                shutil.copyfileobj(res.raw, fh)

        shutil.unpack_archive(tarball_name)
        dirname = '.'.join(tarball_name.split('.')[:2]) + f'.{date.today()}'

        nodes = dict((n.id, n) for n in Node.objects.all())
        with codecs.open(f'{dirname}/nodes.csv', 'r', 'utf-8') as fh:
            reader = csv.DictReader(fh)
            for row in reader:
                node_id = row['node_id']
                node = nodes.get(node_id)
                
                if not node:
                    self.stderr.write(f'{node_id} not found in database')
                    continue
                
                node.latitude = row['lat']
                node.longitude = row['lon']
                node.save()
                self.stdout.write(f'Added location to {node_id}')
        
        os.remove(tarball_name)
        shutil.rmtree(dirname)

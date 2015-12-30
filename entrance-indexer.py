#!/usr/bin/env python

from elasticsearch import Elasticsearch
import util
import argparse
import json

parser = argparse.ArgumentParser(description='Load karst.io entrance data')
parser.add_argument('--server', type=str, default='localhost', help='es server hostname')
parser.add_argument('file', action='store')

args = parser.parse_args()

print args.server
print args.file

es = Elasticsearch()

fptr = open(args.file,'r')
jobj = json.loads(fptr.read())
for entrance in jobj['entrances']:
	lowest_accuracy = -10000
	lowest_accuracy_obj = None
	for coord in entrance['coordinates']:
		if coord['accuracy'] >= lowest_accuracy:
			lowest_accuracy_obj = coord
			lowest_accuracy = coord['accuracy']


	latitude = lowest_accuracy_obj['lat']
	longitude = lowest_accuracy_obj['lon']
	entrance['location'] = {'lat': latitude, 'lon': longitude}
	es.index(index='entrances', doc_type='entrance', body=entrance)

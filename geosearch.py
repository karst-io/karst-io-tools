#!/usr/bin/env python
import argparse
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient

parser = argparse.ArgumentParser(description='Perform entrance search')
parser.add_argument('--server', dest='server', type=str, default='localhost', help='es server hostname')
parser.add_argument('lat', action='store')
parser.add_argument('lon', action='store')
parser.add_argument('dist', action='store', default='1mi')
args = parser.parse_args()

es = Elasticsearch([args.server])

query_body = {
  "query": { 
    "match_all": {}
  },
  "filter": 
  {
      "geo_distance": 
      {
        "distance": args.dist, 
        "location": "%s,%s" % (args.lat, args.lon)
      }
  }
}

res = es.search(index="entrances", body=query_body)
hitcount = res['hits']['total']
print "Results: %s" % hitcount
for hit in res['hits']['hits']:
  print "%s\t%s\t%s\t%s" % (hit['_source']['code'], hit['_source']['name'], hit['_source']['location']['lat'], hit['_source']['location']['lon'])
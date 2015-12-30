from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
import logging
es = Elasticsearch()

indices_delete = ['entrances']

for index in indices_delete:
  if es.indices.exists(index):
    logging.warning("Deleteing index %s", index)
    es.indices.delete(index=index, ignore=[400, 404])


settings = {
"settings": {
  "dynamic": True,
},
"mappings": {
  "entrance": 
  {
    "properties": 
    {
      "name": 
      {
        "type": "string"
      },
      "location":
      {
        "type": "geo_point",
        "lat_lon": True
      }
    }
  }
}
}
es.indices.create(index='entrances', body=settings)

es.index(index='entrances', doc_type='entrance', body={"name":"test","location":{'lat':0, 'lon':0}})
import requests
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

##es.index(index="test", doc_type='tweet', body='{"pin":{"lat" : 40.12,"lon" : -71.34}}')
##es.index(index="test", doc_type='tweet', body='{"pin":{"lat" : 41.12,"lon" : -70.34}}')
##es.index(index="test", doc_type='tweet', body='{"pin":{"lat" : 42.12,"lon" : -69.34}}')

es.index(index="test", doc_type='tweet', body='{"text":"The brown fox jumps over the lazy dog","name":"Richard III","location":{"lat" : 40.12,"lon" : -71.34}}')
es.index(index="test", doc_type='tweet', body='{"text":"The quick fox jumps over the lazy dog","name":"Richard II","location":{"lat" : 41.12,"lon" : -70.34}}')
es.index(index="test", doc_type='tweet', body='{"text":"The quick brown fox jumps over the lazy groundhog","name":"Richard IV","location":{"lat" : 42.12,"lon" : -69.34}}')

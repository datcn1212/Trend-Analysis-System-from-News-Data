from elasticsearch import Elasticsearch
from elasticsearch import helpers

es = Elasticsearch("http://localhost:9202")

def a():
    for i in range(5):
        doc = {
            "_index": "a",
            "_source": {
                "a": i 
            }
        }
        yield doc

helpers.bulk(es, a())

print(es.count(index="a"))
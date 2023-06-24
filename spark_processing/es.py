from elasticsearch import Elasticsearch
from elasticsearch import helpers

class Elastic:

    def __init__(self, path) -> None:
        self.path = path
        self.es = Elasticsearch([self.path])
        self.news_data_mapping = {
            "mappings": {
                "properties": {
                    "Author": {"type": "text"},
                    "Body": {"type": "text"},
                    "Date": {"type": "text"},
                    "Description": {"type": "text"},
                    "Href": {"type": "text"},
                    "Title": {"type": "text"},
                    "Topic": {"type": "text"},
                    "formatted_date": {"type": "text"}
                }
            }
        }

    def count_idx(self, idx_name):
        return self.es.count(idx_name)

    def insert_one(self, idx_name, document, id=None):
        i = self.es.index(index=idx_name, id=id, document=document)
        return i['result']
    
    def insert_bulk(self, generator):
        helpers.bulk(self.es, generator)

    def create_idx_mapping(self, idx_name, mapping):
        self.es.indices.create(index=idx_name, ignore=400, body=mapping)

    # def is_exists_idx(self, idx_name):
    #     return self.es.exists(index=idx_name)

    
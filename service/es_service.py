from elasticsearch import Elasticsearch
from elasticsearch import helpers


class Elastic:

    def __init__(self, path) -> None:
        self.path = path
        self.es = Elasticsearch([self.path])

    def count_idx(self, idx_name):
        return self.es.count(idx_name)

    def insert_one(self, idx_name, document, id=None):
        i = self.es.index(index=idx_name, id=id, document=document)
        return i['result']

    def insert_bulk(self, generator):
        helpers.bulk(self.es, generator)

    def create_idx_mapping(self, idx_name, mapping):
        self.es.indices.create(index=idx_name, ignore=400, body=mapping)

    def get_all_data(self, idx_name):
        query = {
            "query": {
                "match_all": {}
            }
        }
        res = self.es.search(index=idx_name, body=query, size=10000)
        # list of dict {"_index": , "_source": ,...}
        return res["hits"]["hits"]

    def get_data_by_time(self, idx_name, start_time, end_time):
        query = {
            "query": {
                "range": {
                    "formatted_date": {
                        "gte": start_time,
                        "lte": end_time
                    }
                }
            }
        }
        res = self.es.search(index=idx_name, body=query, size=10000)
        return res["hits"]["hits"]

    def count_topic(self, idx_name, start_time, end_time):
        query = {
            "size": 0,
            "query": {
                "range": {
                    "formatted_date": {
                        "gte": start_time,
                        "lte": end_time
                    }
                }
            },
            "aggs": {
                "topics": {
                    "terms": {
                        "field": "Topic",
                        "size": 10
                    }
                }
            }
        }
        res = self.es.search(index=idx_name, body=query)
        # list of {'key': , 'doc_count': ,...}
        return res["aggregations"]["topics"]["buckets"]

    def full_text_search(self, word, idx_name='news_data'):
        query = {
            "query": {
                "match": {
                    "Body": {
                        "query": word
                    }
                }
            }
        }
        res = self.es.search(index=idx_name, body=query)
        return res['hits']['hits']

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from elasticsearch import Elasticsearch
import sparknlp
from es import Elastic
from extract_keyword_sparknlp import ExtractKeywordSparkNLP
from extract_keyword_chatgpt import ExtractKeywordChatGPT
from mapping_topic import *
from pre_processing_text import hash_title

# spark = SparkSession.builder.master("local") \
#                     .appName("Processing data") \
#                     .getOrCreate()

spark = sparknlp.start()
es = Elastic("http://localhost:9202")
extract_nlp = ExtractKeywordSparkNLP(spark)
extract_chatgpt = ExtractKeywordChatGPT()

# create index with mapping
index_name = "news_data"
es.create_idx_mapping(index_name, es.news_data_mapping)


def generator_dct():
    for i in range(len(dct_lst)):
        _doc = {
            '_index': index_name,
            '_id': hash_title(dct_lst[i]['Title']),
            '_source': dct_lst[i]
        }
        yield _doc


def generator_dct_topic():
    for i in range(len(dct_lst)):
        dct = dct_lst[i]
        _doc2 = {
            '_index':  topic_vi_to_en(dct['Topic']),
            '_id': hash_title(dct['Title']),
            '_source': {
                'Title': dct['Title'],
                'formatted_date': dct['formatted_date'],
                'keyword_lst': dct['keyword_lst']
            }
        }
        yield _doc2


# extract keywords
for j in range(18, 23):
    hdfs_path = "hdfs://localhost:9000/newsData/2023/6/" + str(j)
    print(hdfs_path)
    df = spark.read.json(hdfs_path)
    cnt = df.count()
    print('doc_count: ', cnt)
    pandas_df = df.toPandas()

    dct_lst = []

    for i in range(cnt):
        tmp = pandas_df.iloc[i].to_dict()
        try:
            keyword_lst = extract_chatgpt.extract_kw(tmp, num_kw=5)
            tmp['keyword_lst'] = keyword_lst
            dct_lst.append(tmp)

            print(i, keyword_lst)
        except Exception:
            tmp['keyword_lst'] = []
            dct_lst.append(tmp)

    # insert to ES
    res = es.insert_bulk(generator_dct())
    res = es.insert_bulk(generator_dct_topic())

spark.stop()

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from elasticsearch import Elasticsearch
import sparknlp
from extract_keyword_sparknlp import ExtractKeywordSparkNLP
from es import Elastic


# spark = SparkSession.builder.master("local") \
#                     .appName("Processing data") \
#                     .getOrCreate()

spark = sparknlp.start()
es = Elastic("http://localhost:9202")
extract = ExtractKeywordSparkNLP(spark)


# create index with mapping
index_name = "news_data"
es.create_idx_mapping(index_name, es.news_data_mapping)

# extract keywords
hdfs_path = "hdfs://localhost:9000/newsData/2022/11/11"
df = spark.read.json(hdfs_path)
cnt = df.count()
pandas_df = df.toPandas()

def generator_dct():
    for i in range(cnt):
        dct = pandas_df.iloc[i].to_dict()
        keyword_lst = extract.extract_kw(dct)
        dct['keyword_lst'] = keyword_lst
        _doc = {
            '_index': index_name,
            '_source': dct
        }
        yield _doc

# insert to ES
res = es.insert_bulk(generator_dct())

spark.stop()

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from elasticsearch import Elasticsearch
import sparknlp
from extract_keyword import ExtractKeyword
from es import Elastic

# spark = SparkSession.builder.master("local") \
#                     .appName("Processing data") \
#                     .getOrCreate()

spark = sparknlp.start()
es = Elastic("http://localhost:9202")
extract = ExtractKeyword(spark)


# create index with mapping
index_name = "news_data"
es.create_idx_mapping(index_name, es.news_data_mapping)

# extract keywords
hdfs_path = "hdfs://localhost:9000/newsData/2022/11/12"
dct = spark.read.json(hdfs_path).limit(1).toPandas().iloc[0].to_dict()
keyword_lst = extract.extract_kw(dct)
dct['keyword_lst'] = keyword_lst

print(keyword_lst)

# insert to ES
res = es.insert_one(idx_name=index_name, document=dct)
print(res)

spark.stop()

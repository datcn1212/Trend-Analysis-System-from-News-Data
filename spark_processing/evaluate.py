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


# extract keywords
for j in range(6,7):
    hdfs_path = "hdfs://localhost:9000/newsData/2023/7/" + str(j)
    print(hdfs_path)
    df = spark.read.json(hdfs_path)
    cnt = df.count()
    print('doc_count: ', cnt)
    pandas_df = df.toPandas()

    dct_lst = []

    recall_lst = []

    for i in range(cnt):
        tmp = pandas_df.iloc[i].to_dict()
        try:
            keyword_lst = extract_nlp.extract_kw(tmp, num_kw=5)
            tmp['keyword_lst'] = keyword_lst  
            dct_lst.append(tmp) 

            # print(i, keyword_lst)

            # kw_lst by ChatGPT
            kw_lst = es.get_kw_lst_from_title(tmp['Title'])
            # print(i, kw_lst)

            keyword_lst = [keyword.lower().replace('_', ' ') for keyword in keyword_lst]
            kw_lst = [keyword.lower().replace('_', ' ') for keyword in kw_lst]

            # Calculate number of common keywords
            common_keywords = set(keyword_lst) & set(kw_lst)
            num_common_keywords = len(common_keywords)

            # Calculate recall
            recall = num_common_keywords / len(kw_lst)
            print(i, keyword_lst)
            print(i, kw_lst)
            print(f"Recall: {recall}")
            print()

            recall_lst.append(recall)

        except Exception:
            tmp['keyword_lst'] = []
            dct_lst.append(tmp)

    print(sum(recall_lst)/len(recall_lst))
    


spark.stop()

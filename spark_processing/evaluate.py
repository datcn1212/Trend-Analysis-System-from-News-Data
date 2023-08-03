from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from elasticsearch import Elasticsearch
import sparknlp
from es import Elastic
from extract_keyword_sparknlp import ExtractKeywordSparkNLP
from extract_keyword_chatgpt import ExtractKeywordChatGPT
from extract_kw_textrank import ExtractKeywordTextRank
from extract_kw_tfidf import ExtractKeywordTFIDF
from mapping_topic import *
from pre_processing_text import hash_title, preprocessing

# spark = SparkSession.builder.master("local") \
#                     .appName("Processing data") \
#                     .getOrCreate()

spark = sparknlp.start()
es = Elastic("http://localhost:9202")
extract_nlp = ExtractKeywordSparkNLP(spark)
extract_chatgpt = ExtractKeywordChatGPT()
extract_textrank = ExtractKeywordTextRank()
extract_tfidf = ExtractKeywordTFIDF()

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

    vocab_lst = []
    for i in range(cnt): 
        j = pandas_df.iloc[i].to_dict()
        # print(j)
        text = str(j["Title"]) + str(j["Description"]) + str(j["Body"])
        text = preprocessing(text)
        vocab_lst.append(text)
    extract_tfidf.set_vocab(vocab_lst)
    print(len(vocab_lst))

    for i in range(cnt):
        tmp = pandas_df.iloc[i].to_dict()
        try:
            keyword_lst = extract_tfidf.extract_kw(tmp, num_kw=5)
            tmp['keyword_lst'] = keyword_lst  
            dct_lst.append(tmp) 

            # kw_lst by ChatGPT
            kw_lst = es.get_kw_lst_from_title(tmp['Title'])

            keyword_lst = [keyword.lower().replace('_', ' ') for keyword in keyword_lst]
            kw_lst = [keyword.lower().replace('_', ' ') for keyword in kw_lst]

            common_keywords = set(keyword_lst) & set(kw_lst)
            num_common_keywords = len(common_keywords)

            # recall
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

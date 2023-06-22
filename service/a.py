import elasticsearch
from elasticsearch import helpers, Elasticsearch
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

es = Elasticsearch("http://localhost:9202")

query = {
    "query": {
        "term": {
            "formatted_date": "20221111"
        }
    }
}

query1 = {
  "query": {
    "match_all": {}
  }
}

res = es.search(index="news_data", body=query1, size=10000)

# get all keyword 
keywords_list = []
for hit in res["hits"]["hits"]:
    if "keyword_lst" in hit["_source"]:
        keywords_list.extend(hit["_source"]["keyword_lst"])

words_text = " ".join(keywords_list)

wordcloud = WordCloud(width=800, height=400).generate(words_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

from datetime import datetime, timedelta
from flask import Flask, abort, request
from flask_cors import CORS

import elasticsearch
from elasticsearch import helpers, Elasticsearch
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np

from es_service import Elastic

app = Flask(__name__)
CORS(app)

es = Elastic("http://localhost:9202")


@app.route('/all_keywords', methods=['GET'])
def get_all_keywords():
    # get all keywords
    idx_name = 'news_data'
    keywords_list = []
    res = es.get_all_data(idx_name)
    for hit in res:
        if "keyword_lst" in hit["_source"]:
            keywords_list.extend(hit["_source"]["keyword_lst"])
    return {'keywords_list': keywords_list}


# words_text = " ".join(keywords_list)

# wordcloud = WordCloud(width=800, height=400).generate(words_text)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()


if __name__ == "__main__":
    app.run(debug=True)


from datetime import datetime, timedelta
from flask import Flask, abort, request
from flask_cors import CORS

from es_service import Elastic

app = Flask(__name__)
CORS(app)

es = Elastic("http://localhost:9202")


@app.route('/all_keywords', methods=['GET'])
def get_all_keywords():
    # get all keywords
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')

    idx_name = 'news_data'
    keywords_dct = {}

    res = es.get_data_by_time(idx_name, start_time, end_time)

    for hit in res:
        kw = hit["_source"]["keyword_lst"]
        date = hit["_source"]["formatted_date"]
        if date not in keywords_dct.keys():
            keywords_dct[date] = []

        keywords_dct[date].extend(kw)

    return keywords_dct


@app.route('/topic_keywords/<topic>', methods=['GET'])
def get_topic_keywords(topic):
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')

    idx_name = topic
    keywords_dct = {}

    res = es.get_data_by_time(idx_name, start_time, end_time)

    for hit in res:
        kw = hit["_source"]["keyword_lst"]
        date = hit["_source"]["formatted_date"]
        if date not in keywords_dct.keys():
            keywords_dct[date] = []

        keywords_dct[date].extend(kw)

    return keywords_dct

@app.route('/count_topic', methods=['GET'])
def get_count_keyword():
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')

    idx_name = 'news_data'

    res = es.count_topic(idx_name, start_time, end_time)

    dict = {}
    for hit in res:
        dict[hit['key']] = hit['doc_count']

    return dict

if __name__ == "__main__":
    app.run(debug=True)












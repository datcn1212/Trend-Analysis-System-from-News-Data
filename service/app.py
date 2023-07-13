from datetime import datetime, timedelta
from flask import Flask, abort, request
from flask_cors import CORS
import urllib.parse
from es_service import Elastic

app = Flask(__name__)
CORS(app, origins='http://localhost:3000', methods=['GET', 'POST'])


es = Elastic("http://localhost:9202")
topics = [
    "Đời sống",
    "Du lịch",
    "Giải trí",
    "Giáo dục",
    "Khoa học",
    "Kinh doanh",
    "Pháp luật",
    "Sức khỏe",
    "Thế giới",
    "Thể thao",
    "Thời sự",
    "Bất động sản",
    "Số hóa"
]


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
    # keywords_dct = {}

    kw_lst = []
    kw_lst_2 = []
    res = es.get_data_by_time(idx_name, start_time, end_time)

    for hit in res:
        kw = hit["_source"]["keyword_lst"]
        # date = hit["_source"]["formatted_date"]
        # if date not in keywords_dct.keys():
        #     keywords_dct[date] = []

        # keywords_dct[date].extend(kw)
        kw_lst.extend(kw)

    for i in kw_lst:
        kw_lst_2.append(i.replace('_', ' '))
    # return keywords_dct
    return {"data": kw_lst_2}


@app.route('/count_topic', methods=['GET'])
def get_count_keyword():
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')

    idx_name = 'news_data'

    res = es.count_topic(idx_name, start_time, end_time)

    dict = {}
    for hit in res:
        dict[hit['key']] = hit['doc_count']

    for x in topics:
        if x not in dict.keys():
            dict[x] = 0

    return dict


@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word')
    res = es.full_text_search(urllib.parse.unquote(word))
    return {'data': [re['_source'] for re in res[:5]]}


@app.route('/count_word_by_time', methods=['GET'])
def count_word_by_time():
    word = request.args.get('word')
    start_time = request.args.get('startTime')
    end_time = request.args.get('endTime')

    res = es.exact_match_in_time(urllib.parse.unquote(word), start_time, end_time)
    return {'data': res}


if __name__ == "__main__":
    app.run(debug=True)
## Trend Analysis System from News Data

### Start Docker container
* `cd` to specific folder: hadoop, elasticsearch_singlenode, spark_processing
* run `docker-compose up`

### 1. Crawl data: VnExpress, Vietnamnet 
* crawl from vnexpress: `cd crawler/` & `crawler crawl vnexpress_main --logfile log_vnex.txt`
* crawl from vietnamnet `cd crawler/` & `crawler crawl vietnamnet_main --logfile log_vietnamnet.txt`
* Note: change proxy if needed in *crawler/proxies.py* 

### 2. Process data:
* change file *spark_processing* to desire method (YAKE, TextRank, TF-IDF, OpenAI API) and change date
* run command `python3 spark_processing/process.py` 
* to evaluate method (recall@k, use label from ChatGPT's result): `python3 spark_processing/evaluate.py`
* Note: change API key if needed in *spark_processing/extract_kw_chatgpt.py*

### 3. Build the web
* Run Flask: `python3 service/app.py`
* Run React App: `cd ui` & `npm start`
# Run crawler (save data to data.json)
scrapy crawl crawler -o data.json 

# Save log to logfile
scrapy crawl crawler -o data.json --logfile log.txt


# Config proxy for crawling
- get proxy from: https://proxy2.webshare.io/proxy/rotating?filters=eyJjb3VudHJ5RmlsdGVyIjpbXX0%253D
- change information in proxies.py
import scrapy
from crawler.items import CrawlerItem

class ASpider(scrapy.Spider):
    name = "a"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/cong-ty-trung-quoc-che-tao-tau-dem-tu-1-000-km-h-4604265.html"]

    def parse(self, response):
        item = CrawlerItem()
        item['User'] = response.css(".Normal::text").getall()[0:-2]
        yield item      
        

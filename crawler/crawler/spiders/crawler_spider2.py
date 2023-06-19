import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import os
import datetime

# from scrapy_splash import scrapy.Request

BASE_URL = "https://vnexpress.net"

TOPICS =  {
    "thoi-su": "Thời sự",
    "the-gioi": "Thế giới",
    "kinh-doanh": "Kinh doanh",
    "khoa-hoc": "Khoa học",
    "giai-tri": "Giải trí",
    "du-lich": "Du lịch",
    "giao-duc": "Giáo dục",

}

TOPICS_ID =  {
    "thoi-su": "1001005",
    "the-gioi": "1001002",
    "kinh-doanh": "1003159",
    "khoa-hoc": "1001009",
    "giai-tri": "1002691"
}

class CrawlerSpider(Spider):
    name = "crawler2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
        self.start_urls = []
        self.folder_path = "vnexpress"


        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        dir_path = os.getcwd() + "/urls"
        for filename in os.listdir(dir_path):
            if filename.endswith(".txt"):  
            # if filename.endswith("test.txt"):
                file_path = os.path.join(dir_path, filename)
                with open(file_path, "r") as file:
                    for line in file:
                        self.start_urls.append(line)


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse_news)      

    def parse_news(self, response):

        topic = response.css('ul.breadcrumb li a::attr(title)').extract_first()
        title = response.css('h1.title-detail::text').extract_first()
        href = response.url
        author = response.css('p.Normal strong::text').getall()

        if len(author)==0: 
            author = response.css('p.author_mail strong::text').getall()
        if len(author)==0:
            author = response.css('div.width-detail-photo p strong::text').getall()

        date = response.css('span.date::text').extract_first()
        description = response.css('p.description::text').extract_first()
        body = response.css('p.Normal::text').getall()
        comment = response.css('p.full_content::text').getall()
        
        if topic is None:
             pass
        else:
            item = CrawlerItem()
            item['Topic'] = topic
            item['Date'] = date
            if author:
                item['Author'] = author[-1]
            else:
                item['Author'] = None
            item['Title'] = title
            item['Href'] = href          
            item['Description'] =  description
            item['Body'] = ' '.join(body)
            # item['Comment'] = comment
            yield item
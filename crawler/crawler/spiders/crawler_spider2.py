import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import os
import datetime

class CrawlerSpider(Spider):
    name = "crawler2"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
        self.start_urls = []
        
        dir_path = os.getcwd() + "/urls"
        for filename in os.listdir(dir_path):
            if filename.endswith("test.txt"):  
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
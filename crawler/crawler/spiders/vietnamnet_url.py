import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import os
import datetime
import time

BASE_URL = "https://vietnamnet.vn"

TOPICS_ID = {
    'chinh-tri': 0,
    # 'van-hoa': 0,
    # 'thong-tin-truyen-thong': 0,
    # 'thoi-su': 1001005,
    # 'doi-song': 1002966,
    # 'du-lich': 1003231,
    # 'the-gioi': 1001002,
    # 'the-thao': 1002565,
    # 'phap-luat': 1001007,
    # 'giai-tri': 1002691,
    # 'giao-duc': 1003497,
    # 'bat-dong-san': 1005628,
    # 'kinh-doanh': 1003159,
    # 'suc-khoe': 1003784,
    # 'dan-toc-ton-giao':0,
}


class CrawlerSpider(Spider):
    name = "vietnamnet_main"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = []
        self.max_page = 1
        self.title_lst = []

        for topic in list(TOPICS_ID.keys()):
            for i in range(self.max_page):
                url = 'https://vietnamnet.vn/' + str(topic) + '-page' + str(i)
                self.start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        lst_news = response.css("h3.verticalPost__main-title.vnn-title.title-bold a::attr(href)").getall()
        lst_news.extend(response.css("h3.horizontalPost__main-title.vnn-title.title-bold a::attr(href)").getall())
       
        for news in lst_news:
            if news.startswith('/'): 
                news = 'https://vietnamnet.vn' + news
            yield scrapy.Request(news, self.parse_news)

    def parse_news(self, response):
        topic = response.css('ul.breadcrumb li a::attr(title)').extract_first()
        title = response.css('h1.title-detail::text').extract_first()
        href = response.url
        author = response.css('p.Normal strong::text').getall()

        if len(author) == 0:
            author = response.css('p.author_mail strong::text').getall()
        if len(author) == 0:
            author = response.css(
                'div.width-detail-photo p strong::text').getall()

        date = response.css('span.date::text').extract_first()
        description = response.css('p.description::text').extract_first()
        body = response.css('p.Normal::text').getall()
        comment = response.css('p.full_content::text').getall()

        item = CrawlerItem()
        item['Topic'] = topic
        item['Date'] = date
        if author:
            item['Author'] = author[-1]
        else:
            item['Author'] = None
        item['Title'] = title       
        item['Href'] = href
        item['Description'] = description
        item['Body'] = ' '.join(body)
        
        date_part = date.split(", ")[1]
        date = datetime.datetime.strptime(date_part, "%d/%m/%Y")
        formatted_date= date.strftime("%Y%m%d")

        # date after 1/5/2023
        if formatted_date >= '20230501':
            if title not in self.title_lst:
                self.title_lst.append(title)
                yield item


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
    'van-hoa': 0,
    'thong-tin-truyen-thong': 0,
    'thoi-su': 1001005,
    'doi-song': 1002966,
    'du-lich': 1003231,
    'the-gioi': 1001002,
    'the-thao': 1002565,
    'phap-luat': 1001007,
    'giai-tri': 1002691,
    'giao-duc': 1003497,
    'bat-dong-san': 1005628,
    'kinh-doanh': 1003159,
    'suc-khoe': 1003784,
    'dan-toc-ton-giao':0,
}


class CrawlerSpider(Spider):
    name = "vietnamnet_main"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = []
        self.max_page = 25
        self.title_lst = []

        for topic in list(TOPICS_ID.keys()):
            for i in range(self.max_page):
                url = 'https://vietnamnet.vn/' + str(topic) + '-page' + str(i)
                self.start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        lst_news = response.css(
            "h3.verticalPost__main-title.vnn-title.title-bold a::attr(href)").getall()
        lst_news.extend(response.css(
            "h3.horizontalPost__main-title.vnn-title.title-bold a::attr(href)").getall())

        for news in lst_news:
            if news.startswith('/'):
                news = 'https://vietnamnet.vn' + news
            yield scrapy.Request(news, self.parse_news)

    def parse_news(self, response):
        topic = response.css(
            'div.bread-crumb-detail.sm-show-time ul li a::attr(title)').extract_first()
        title = response.css('h1.content-detail-title::text').extract_first()
        href = response.url
        author = response.css(
            'p.article-detail-author__info span.name a::attr(title)').extract_first()

        # if len(author) == 0:
        #     author = response.css('p.author_mail strong::text').getall()
        # if len(author) == 0:
        #     author = response.css(
        #         'div.width-detail-photo p strong::text').getall()

        date = response.css(
            'div.bread-crumb-detail__time::text').extract_first().strip()
        description = response.css(
            'h2.content-detail-sapo.sm-sapo-mb-0::text').extract_first()
        body = response.css(
            'div.maincontent.main-content p::text, div.maincontent.main-content p a::text, div.maincontent.main-content p strong::text').getall()
        # comment = response.css('p.full_content::text').getall()

        item = CrawlerItem()
        item['Topic'] = topic
        item['Date'] = date
        item['Author'] = author
        item['Title'] = title
        item['Href'] = href
        item['Description'] = description
        item['Body'] = ' '.join(body).replace('\xa0', '').replace('  ', ' ')

        date_object = date.split(' ')[2]
        day, month, year = date_object.split("/")
        formatted_date = year+month+day
        item['formatted_date'] = formatted_date

        # # date after 1/6/2023
        if formatted_date >= '20230601':
            if title not in self.title_lst:
                self.title_lst.append(title)
                yield item


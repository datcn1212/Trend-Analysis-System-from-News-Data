import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import os
import datetime
import time

# from scrapy_splash import scrapy.Request

BASE_URL = "https://vnexpress.net"

TOPICS_ID = {
    # 'thoi-su': 1001005,
    # 'doi-song': 1002966,
    'du-lich': 1003231,
    # 'the-gioi': 1001002,
    # 'the-thao': 1002565,
    # 'phap-luat': 1001007,
    # 'giai-tri': 1002691,
    # 'giao-duc': 1003497,
    # 'bat-dong-san': 1005628,
    # 'khoa-hoc': 1001009,
    # 'kinh-doanh': 1003159,
    # 'so-hoa': 1002592,
    # 'gia-dinh': 1002966,
    # 'suc-khoe': 1003784
}


class CrawlerSpiderSetUp(Spider):
    name = "crawler_setup"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = ['https://vnexpress.net/thoi-su']

        current_datetime = datetime.datetime.now().replace(
            hour=7, minute=0, second=0, microsecond=0)
        self.current_timestamp = int(current_datetime.timestamp())
        self.page = 1
        self.title_lst = []

        # for topic in list(TOPICS_ID.keys()):
        #     # 1/5/2023 -> 15/6/2023
        #     url = f"https://vnexpress.net/category/day?cateid={TOPICS_ID[topic]}&fromdate=1682899200&todate=1686787200&allcate={TOPICS_ID[topic]}"
        #     self.start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        time.sleep(10)
        lst_news = response.css("h3.title-news a::attr(href)").getall()
        for news in lst_news:
            yield scrapy.Request(news, self.parse_news)

        next_page_url_ = response.css("a.btn-page.next-page::attr(href)").get()
        next_page_url = "https://vnexpress.net" + str(next_page_url_)
        print(next_page_url)

        if next_page_url_:
            self.page += 1
            next_page_url = response.url[:-1] + str(self.page)
            yield scrapy.Request(next_page_url, self.parse)
        else:
            return

    def parse_news(self, response):
        time.sleep(1)
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
        self.title_lst.append(title)
        item['Href'] = href
        item['Description'] = description
        item['Body'] = ' '.join(body)
        # item['Comment'] = comment
        if title not in self.title_lst:
            yield item


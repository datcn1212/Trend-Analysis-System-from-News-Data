import scrapy
from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem
import os
import datetime

# from scrapy_splash import scrapy.Request

BASE_URL = "https://vnexpress.net"

TOPICS_ID = {
    'thoi-su': 1001005,
    # 'doi-song': 1002966,
    # 'du-lich': 1003231,
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


class CrawlerSpider(Spider):
    name = "crawler"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.start_urls = []
        self.folder_path = "vnexpress"

        current_datetime = datetime.datetime.now().replace(
            hour=7, minute=0, second=0, microsecond=0)
        self.current_timestamp = int(current_datetime.timestamp())

        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)

        for topic in list(TOPICS_ID.keys()):
            topic_path = self.folder_path + '/' + topic
            if not os.path.exists(topic_path):
                os.makedirs(topic_path)

            # url = f"https://vnexpress.net/category/day?cateid={TOPICS_ID[topic]}&fromdate=1681344000&todate={self.current_timestamp}"
            url = f"https://vnexpress.net/category/day?cateid={TOPICS_ID[topic]}&fromdate=1682899200&todate=1686787200&allcate={TOPICS_ID[topic]}"
            self.start_urls.append(url)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):

        lst_news = response.css("h3.title-news a::attr(href)").getall()
        for news in lst_news:
            yield scrapy.Request(news, self.parse_news)

        next_page_url_ = response.css("a.btn-page.next-page::attr(href)").get()
        next_page_url = "https://vnexpress.net" + str(next_page_url_)
        print(next_page_url)
        if next_page_url_:
            yield scrapy.Request(next_page_url, self.parse)
        else:
            return

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
        # item['Comment'] = comment
        yield item

from scrapy import Spider
from scrapy.selector import Selector
from crawler.items import CrawlerItem

class CrawlerSpider(Spider):
    name = "crawler"
    allowed_domains = ["vnexpress.net"]
    start_urls = [
        "https://vnexpress.net/zte-blade-wave-3-ra-mat-phien-ban-vang-3372151.html",
    ]

    def parse(self, response):
        item = CrawlerItem()
        item['User'] =  response.css('p.description ::text').extract_first()
        yield item
        # for question in questions:
        #     item = CrawlerItem()

        #     item['User'] = question.xpath(
        #         'p[@class="description"]/text()').extract_first()
            # item['Comment'] = question.xpath(
            #     'div[@class="question"]/text()').extract_first()
            # item['Time'] = question.xpath(
            #     'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()

            # yield item

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
        
    Topic = scrapy.Field()
    Date = scrapy.Field()
    Author = scrapy.Field()
    Title = scrapy.Field()
    Href = scrapy.Field()
    Description = scrapy.Field()
    Body = scrapy.Field()
    Comment = scrapy.Field()
    formatted_date = scrapy.Field()
    


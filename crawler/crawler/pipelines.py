# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter

class CrawlerPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        error_lst = ["", " ", ", ", None]
        if adapter.get("Body") in error_lst:
            raise DropItem(f"Missing author in {item}")
        else:
            return item
        
        # return item
    def open_spider(self, spider):
        self.filename = "x.json"
        self.jsonfile  = open(self.filename, 'wb')
        self.exporter = JsonItemExporter(self.jsonfile, encoding='utf-8')
        self.exporter.start_exporting()

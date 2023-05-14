# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
import json
from hdfs import InsecureClient
from pyspark.sql import SparkSession

class CrawlerPipeline:

    def open_spider(self, spider):
        self.file = open("data1.json", "w", encoding='utf-8')
        self.file.write('[\n')
        # HDFS client
        # self.client = InsecureClient('http://localhost:9000', user='root')

    def close_spider(self, spider):
        self.file.write('{}]')
        self.file.close()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        error_lst = ["", " ", ", ", None]
        if adapter.get("Body") in error_lst:
            raise DropItem(f"Missing author in {item}")
        else:
            # Save to file
            line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + ",\n"
            self.file.write(line)

            # Save to HDFS

            spark = SparkSession.builder \
                .appName("Write to HDFS") \
                .getOrCreate()
            data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
            df = spark.createDataFrame(data, ["Name", "Age"])
            hdfs_path = "hdfs://localhost:9000/user/root/data.parquet"
            df.write.parquet(hdfs_path)

            # hdfs_output_path = '/user/caodat/file.json'
            # with self.client.write(hdfs_output_path, overwrite=True) as file:
            #     file.write(json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False))

            return item
        
        # return item
    # def open_spider(self, spider):
    #     self.filename = "x.json"
    #     self.jsonfile  = open(self.filename, 'wb')
    #     self.exporter = JsonItemExporter(self.jsonfile, encoding='utf-8')
    #     self.exporter.start_exporting()

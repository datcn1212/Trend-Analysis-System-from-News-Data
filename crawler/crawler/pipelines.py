from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
import json
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import SparkSession
import datetime

class CrawlerPipeline:

    def __init__(self):
         pass
        # self.spark = SparkSession.builder \
        #         .appName("Write to HDFS") \
        #         .getOrCreate()
        # self.schema = StructType([
        #                 StructField("Topic", StringType(), nullable=False),
        #                 StructField("Date", StringType(), nullable=True),
        #                 StructField("Author", StringType(), nullable=True),
        #                 StructField("Title", StringType(), nullable=False),
        #                 StructField("Href", StringType(), nullable=False),
        #                 StructField("Description", StringType(), nullable=True),
        #                 StructField("Body", StringType(), nullable=False),
        #                 StructField("formatted_date", StringType(), nullable=False)
        #             ])

    # def open_spider(self, spider):
        # self.file = open("vnexpress_urls/url.txt", "a", encoding='utf-8')
        # self.file1 = open("data.json", "w", encoding='utf-8')

    # def close_spider(self, spider):
        # self.file.close()
        # self.file1.close()
        # self.spark.stop()

    def process_item(self, item, spider):
        # adapter = ItemAdapter(item)
        # error_lst = ["", " ", ", ", None]
        # if adapter.get("Body") in error_lst:
        #     raise DropItem(f"Missing body in {item}")
        # else:
        #     # item_line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) 
        #     # self.file1.write(item_line+ ",\n")
            
            # i = ItemAdapter(item).asdict()

            # self.file.write(i['Href']+ "\n")
        #     date_part = i["Date"].split(", ")[1]
        #     date = datetime.datetime.strptime(date_part, "%d/%m/%Y")
        #     year = str(date.year)
        #     month = str(date.month)
        #     day = str(date.day)
        #     i["formatted_date"] = date.strftime("%Y%m%d")

        #     hdfs_path = "hdfs://localhost:9000/newsData/" + year + "/" + month + "/" + day 

        #     df = self.spark.createDataFrame([i], self.schema)
            # df.write.mode("append").json(hdfs_path)
            return item

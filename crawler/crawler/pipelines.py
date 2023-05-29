# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
from scrapy.exporters import JsonItemExporter
import json
from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql import SparkSession

class CrawlerPipeline:

    def __init__(self):
        self.spark = SparkSession.builder \
                .appName("Write to HDFS") \
                .getOrCreate()
        self.hdfs_path = "hdfs://localhost:9000/datcao/test1.parquet"
        self.lst_data = []
        self.schema = StructType([
                        StructField("Topic", StringType(), nullable=False),
                        StructField("Date", StringType(), nullable=True),
                        StructField("Author", StringType(), nullable=True),
                        StructField("Title", StringType(), nullable=False),
                        StructField("Href", StringType(), nullable=False),
                        StructField("Description", StringType(), nullable=True),
                        StructField("Body", StringType(), nullable=False)
                    ])

    def open_spider(self, spider):
        self.file = open("data1.json", "w", encoding='utf-8')
        self.file.write('[\n')

    def close_spider(self, spider):
        self.file.write('{}]')
        self.file.close()
        # save final dataframe to HDFS
        df = self.spark.createDataFrame(self.lst_data, self.schema)
        df.write.mode("overwrite").json(self.hdfs_path)

        # stop session
        self.spark.stop()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        error_lst = ["", " ", ", ", None]
        if adapter.get("Body") in error_lst:
            raise DropItem(f"Missing author in {item}")
        else:
            # Save to file
            item_line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) 
            self.file.write(item_line+ ",\n")

            # Union new item to dataframe
            i = ItemAdapter(item).asdict()
            self.lst_data.append(i)
            return item

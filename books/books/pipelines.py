# -*- coding: utf-8 -*-
import logging
import psycopg2


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class BooksPipeline(object):

    # calls before open_spider
    @classmethod
    def from_crawler(cls, crawler):
        logging.warning(crawler.settings.get("FEED_EXPORT_ENCODING"))

    # calls once when spider starts crawl
    def open_spider(self, spider):
        logging.warning("SPIDER OPENED FROM PIPELINE")

    # calls each request between open_spider and close_spider
    def process_item(self, item, spider):
        logging.info("PROCESSED ITEM")
        return item

    # calls once after spider finished crawling
    def close_spider(self, spider):
        logging.warning("SPIDER CLOSED FROM PIPELINE")


class PostgreSQLPipeline:

    def open_spider(self, spider):
        self.connection = psycopg2.connect("postgresql://async:Dexter89!@localhost/scrapy_db")
        self.cursor = self.connection.cursor()
        self.formula = """insert into books(title, price, star) values (%s, %s, %s)"""

    def process_item(self, item, spider):
        data = item["title"], item["price"], item["star"]
        self.cursor.execute(self.formula, data)
        return item

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

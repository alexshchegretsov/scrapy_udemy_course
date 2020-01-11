# -*- coding: utf-8 -*-

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from books.spiders.book_spider import BookSpiderSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(BookSpiderSpider)
process.start()

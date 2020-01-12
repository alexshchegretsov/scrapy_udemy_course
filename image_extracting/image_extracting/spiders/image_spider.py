# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from image_extracting.items import ImageExtractingItem


class ImageSpider(scrapy.Spider):
    name = "image_spider"
    start_urls = ["http://books.toscrape.com"]

    def parse(self, response):
        divs = response.css("article.product_pod")
        for div in divs:
            # create loader for our item, defined in items.py
            loader = ItemLoader(item=ImageExtractingItem(), selector=div)
            rel_url = div.css("div.image_container img::attr(src)").get()
            absolute_image_url = response.urljoin(rel_url)

            loader.add_value("image_urls", absolute_image_url)
            loader.add_css("book_name", "h3>a::attr(title)")
            yield loader.load_item()

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst


def book_name_serializer(value):
    return value.rstrip()


class ImageExtractingItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    book_name = scrapy.Field(output_processor=TakeFirst(), serializer=book_name_serializer)

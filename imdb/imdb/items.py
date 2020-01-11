# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
import unicodedata


# like FEED_EXPOR_ENCODING = "utf-8"
def serializer_title(data: str):
    new_str = unicodedata.normalize("NFKD", data)
    return new_str.rstrip()

class ImdbItem(scrapy.Item):
    title = scrapy.Field(serializer=serializer_title)
    year = scrapy.Field()
    duration = scrapy.Field()
    genre = scrapy.Field()
    rating = scrapy.Field()


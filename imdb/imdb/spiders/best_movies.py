# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ImdbItem


class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
    allowed_domains = ['imdb.com']
    start_urls = ["https://www.imdb.com/chart/top/?ref_=nv_mv_250"]

    rules = (
        Rule(LinkExtractor(restrict_css="tbody td.titleColumn>a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        title = response.css("div.title_bar_wrapper div.title_wrapper>h1::text").get()
        year = response.css("div.title_bar_wrapper div.title_wrapper>h1>span>a::text").get()
        duration = response.css("div.title_bar_wrapper div.title_wrapper time ::text").get().strip()
        genre = response.css("div.title_bar_wrapper div.subtext a ::text").get()
        rating = response.css("div.title_bar_wrapper div.ratingValue>strong::attr(title)").get().split()[0]
        return ImdbItem(
            title=title,
            year=year,
            duration=duration,
            genre=genre,
            rating=rating
        )

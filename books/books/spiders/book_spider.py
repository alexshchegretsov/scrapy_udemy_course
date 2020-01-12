# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from http_request_randomizer.requests.useragent.userAgent import UserAgentManager as User_Agent

star_mapper = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


class BookSpiderSpider(CrawlSpider):
    name = 'book_spider'
    allowed_domains = ['books.toscrape.com']
    # no need start_url if start_requests exists
    def start_requests(self):
        yield scrapy.Request(
            url="http://books.toscrape.com",
            headers={"User-Agent": User_Agent().get_random_user_agent()}
        )

    # rules order do matter
    rules = (
        # html for detail parse
        Rule(
            LinkExtractor(restrict_css="ol.row div.image_container>a"),
            callback='parse_item',
            follow=True,
            process_request="set_user_agent"
        ),
        # main pages for first Rule
        Rule(LinkExtractor(restrict_css="li.next>a"), process_request="set_user_agent"),
    )

    def set_user_agent(self, request):
        request.headers["User-Agent"] = User_Agent().get_random_user_agent()
        print("Changed")
        return request

    def parse_item(self, response):
        # use sibling compinator
        star_txt = response.css("div.col-sm-6.product_main p.instock.availability~p::attr(class)").get().split()[-1]
        yield {
            "title": response.css("div.col-sm-6.product_main>h1::text").get(),
            "price": response.css("p.price_color::text").get(),
            "star": star_mapper[star_txt],
            # "user_agent": response.request.headers["User-Agent"]
        }

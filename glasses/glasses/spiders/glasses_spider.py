# -*- coding: utf-8 -*-
import scrapy


class GlassesSpiderSpider(scrapy.Spider):
    name = 'glasses_spider'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers']

    def parse(self, response):
        divs = response.css("div.prlist.row div.col-sm-6.col-md-4.m-p-product")
        for div in divs:
            product_link = div.css("div.pimg.default-image-front>a::attr(href)").get()
            product_image_link = div.css("div.pimg.default-image-front>a>img::attr(src)").get()
            product_name = div.css("div.row>p>a::text").get()
            product_price = div.css("span.pull-right::text").get()

            yield {
                "product_link": product_link,
                "product_image_link": product_image_link,
                "product_name": product_name,
                "product_price": product_price
            }

        hrefs = response.css("ul.pagination li>a")
        guess_next = hrefs[-1].css("::attr(rel)").get()
        if guess_next:
            next_url = hrefs[-1].css("::attr(href)").get()
            yield response.follow(next_url)

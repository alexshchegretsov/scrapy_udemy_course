# -*- coding: utf-8 -*-
import scrapy
import logging


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # never ever start with http://... - it will not work
    allowed_domains = ['www.worldometers.info']
    # by default scrapy add http protocol - change it if use other one (https)
    start_urls = ['http://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.css("td>a")
        for country in countries:
            country_name = country.css("::text").get()
            country_related_url = country.css("::attr(href)").get()
            yield response.follow(
                url=country_related_url,
                callback=self.parse_country,
                meta={"country_name": country_name}
            )

    def parse_country(self, response):
        trs = response.css("div.table-responsive:nth-child(7) > table:nth-child(1) tbody>tr")
        for tr in trs:
            year = tr.css("td::text").get()
            population = tr.css("td>strong::text").get()
            yield {
                "country": response.request.meta["country_name"],
                "year": year,
                "population": population
            }

# -*- coding: utf-8 -*-
import scrapy


class DebtSpiderSpider(scrapy.Spider):
    name = 'debt_spider'
    allowed_domains = ['www.worldpopulationreview.com']
    start_urls = ['http://www.worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        trs = response.css("tbody>tr")
        for tr in trs:
            country = tr.css("td>a::text").get()
            data = tr.css("td::text").getall()
            gdp_debt_percent, population = data if len(data) > 1 else [data[0], "No population data"]

            yield {
                "country": country,
                "gdp_debt": gdp_debt_percent,
                "population": population
            }

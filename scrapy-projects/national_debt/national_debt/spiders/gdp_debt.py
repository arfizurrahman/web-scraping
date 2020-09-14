# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['https://worldpopulationreview.com']
    start_urls = [
        'https://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        

# -*- coding: utf-8 -*-
import scrapy


class OnlinescraperSpider(scrapy.Spider):
    name = 'onlineScraper'
    allowed_domains = ['https://www.bbc.com/nepali/news']
    start_urls = ['http://https://www.bbc.com/nepali/news/']

    def parse(self, response):
        pass

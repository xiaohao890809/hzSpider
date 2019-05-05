# -*- coding: utf-8 -*-
import scrapy


class Hz1Spider(scrapy.Spider):
    name = 'hz1'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        item = {}
        item['a'] = 'b'
        yield item

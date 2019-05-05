# -*- coding: utf-8 -*-
import scrapy
import logging

logger = logging.getLogger(__name__)

class Hz2Spider(scrapy.Spider):
    name = 'hz2'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        for i in range(10):
            item = {}
            item['hz2'] = 'xiaohao2'
            # logging.warning(item)
            # 下面这种方式更常用
            logger.warning(item)
            yield item

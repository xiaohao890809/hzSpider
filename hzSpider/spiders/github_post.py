# -*- coding: utf-8 -*-
import scrapy
import re


class GithubPostSpider(scrapy.Spider):
    name = 'github_post'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response, # 自动从response中寻找form表单
            formdata={"login":"xiaohao890809", "password":"XHmnbQWE7658285"},
            callback=self.after_login
        )

    def after_login(self, response):
        print(re.findall("xiaohao890809", response.body.decode()))

# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HrCrawlSpider(CrawlSpider):
    name = 'hr_crawl'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['title'] = response.xpath("//td[@id='sharetitle']/text()").extract_first()
        item['acquire'] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)
        # return item

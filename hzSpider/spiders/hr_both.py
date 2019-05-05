# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HrBothSpider(CrawlSpider):
    name = 'hr_both'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item = {}
            item['title'] = tr.xpath("./td[1]/a/text()").extract_first()
            item['href'] = 'https://hr.tencent.com/' + tr.xpath("./td[1]/a/@href").extract_first()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item':item}
            )
        return item

    def parse_detail(self, response):
        item = response.meta['item']
        item['acquire'] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)

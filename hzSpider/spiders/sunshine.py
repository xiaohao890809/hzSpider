# -*- coding: utf-8 -*-
import scrapy
from hzSpider.items import SunspiderItem


class SunshineSpider(scrapy.Spider):
    name = 'sunshine'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?']

    def parse(self, response):
        tr_list = response.xpath("//div[@class='greyframe']//table[2]//tr//table//tr")
        print(len(tr_list))
        for tr in tr_list:
            item = SunspiderItem()
            # .不能掉了
            item['title'] = tr.xpath(".//td[2]//a[@class='news14']//@title").extract_first()
            item['href'] = tr.xpath(".//td[2]//a[@class='news14']//@href").extract_first()
            item['publish_date'] = tr.xpath(".//td[last()]//text()").extract_first()

            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={'item':item}
            )

        # 翻页功能
        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )


    def parse_detail(self, response):
        item = response.meta['item']
        item['content'] = response.xpath("//div[@class='wzy1']//table[2]//tr[1]//text()").extract()
        item['content_img'] = response.xpath("//td[@class='txt16_3']//img//@src").extract()
        item['content_img'] = ['http://wz.sun0769.com' + i for i in item['content_img']]
        yield item

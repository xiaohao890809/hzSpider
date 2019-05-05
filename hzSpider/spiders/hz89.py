# -*- coding: utf-8 -*-
import scrapy


class Hz89Spider(scrapy.Spider):
    name = 'hz89' # 爬虫名
    allowed_domains = ['itcast.cn'] # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] # 最开始请求的url地址

    def parse(self, response):
        # 处理start_url地址对应的相应
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1)

        # 分组显示
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            # item['name'] = li.xpath(".//h3/text()").extract()[0]
            item['name'] = li.xpath(".//h3/text()").extract_first() # extract_first更常用
            item['title'] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            # 格式必须是 Request, BaseItem, dict or None
            yield item
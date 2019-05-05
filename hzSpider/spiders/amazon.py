# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmazonSpider(RedisCrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.cn']
    # start_urls = ['https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/b/ref=sd_allcat_books_l1?ie=UTF8&node=658390051']
    redis_key = 'amazon'

    rules = (
        # 匹配大分类的url和小分类的url
        # Rule(LinkExtractor(restrict_xpaths=("//div[@aria-live='polite']/li",)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='leftNav']/ul[1]/ul/div/li",)), follow=True),
        # 匹配图书的url地址
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)), callback='parse_book_detail'),
        # Rule(LinkExtractor(restrict_xpaths=("//div[@class='a-row']/div[1]/a",)), callback='parse_book_detail'),
        # 列表页翻页
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='pagn']",)), follow=True),
    )

    def parse_book_detail(self, response):
        print(response.url)
        item = {}
        item["book_title"] = response.xpath("//span[@id='productTitle']/text()").extract_first()
        item['book_publish_date'] = response.xpath("//h1[@id='title']/span[last()]/text()").extract_first()
        item['book_author'] = response.xpath("//div[@id='bylineInfo']/span/a/text()").extract()
        # item['book_img'] = response.xpath("//div[@id='img-canvas']/img/@src").extract_first()
        item['book_price'] = response.xpath("//div[@id='soldByThirdParty']/span[2]/text()").extract_first()
        item['book_cate'] = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li[not(@class)]/span/a/text()").extract()
        item['book_cate'] = [i.strip() for i in item['book_cate']]
        item['book_press'] = response.xpath("//b[text()='出版社:']/../text()").extract_first()
        item['book_desc'] = response.xpath("//noscript/div/text()").extract()
        item['book_desc'] = [i.strip() for i in item['book_desc'] if len(i.strip())>0 and i != '海报：']
        print(item)


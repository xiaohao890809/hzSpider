# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/248965935/profile']

    def start_requests(self):
        cookies = "anonymid=jqpacc0i4eh2re; depovince=ZGQT; _r01_=1; JSESSIONID=abcM4DE98_8lS_2hu7hLw; ick_login=94fa5e6e-2259-463b-881d-df55cf5d31b4; first_login_flag=1; ln_uact=xiaohao890809@126.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20140707/2350/h_main_shjp_279f00034af41986.jpg; jebecookies=925db273-3e75-49f0-bacd-abacee2a6b81|||||; _de=3CDE58455645D198DBFE84ABF93BB1C2016C1A0D299EDE5B; p=4a5221b4c010579663433479643c85865; t=3876d753078939e088d5fc2d2a1b93225; societyguester=3876d753078939e088d5fc2d2a1b93225; id=248965935; xnsid=b8125ddb; ver=7.0; loginfrom=null; wp=1; wp_fold=1"
        cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(re.findall('肖浩', response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/248965935/profile?v=info_timeline",
            callback=self.parse_detail
        )

    def parse_detail(self, response):
        print(re.findall('肖浩', response.body.decode()))

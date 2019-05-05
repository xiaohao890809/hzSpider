# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import re
import logging
logger = logging.getLogger(__name__)

client = MongoClient()
collection = client["tencent"]["hr"]

class HzspiderPipeline(object):
    def process_item(self, item, spider):
        # item['hello'] = 'world'
        if spider.name == 'hz89':
            print(item)
        elif spider.name == 'hz2':
            logger.warning('*'*10)
        elif spider.name == 'hr':
            print(item)
            # mongo只支持字典形式
            # collection.insert(dict(item))
        elif spider.name == 'sunshine':
            item['content'] = self.process_content(item['content'])
            print(item)
        return item

    def process_content(self, content):
        content = [re.sub(r"\xa0|\s","",i) for i in content]
        content = [i for i in content if len(i)>0] # 去掉列表中的空字符串
        return content

# class HzspiderPipeline1(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item
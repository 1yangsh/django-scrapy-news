# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter
from scrapy.exporters import JsonItemExporter
from news.models import New

from pydispatch import dispatcher
from scrapy import signals


class MyscraperPipeline(object):

    def __init__(self, unique_id, *args, **kwargs):
        self.unique_id = unique_id
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            unique_id=crawler.settings.get('unique_id'),
        )

    def process_item(self, item, spider):
        new_item = New()
        new_item.unique_id = self.unique_id
        new_item.title = item['title']
        new_item.writer = item['writer']
        new_item.preview = item['preview']

        new_item.save()
        return item

    def spider_closed(self, spider):
        print('SPIDER FINISHED!')

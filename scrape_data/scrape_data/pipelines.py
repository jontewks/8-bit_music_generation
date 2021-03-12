# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from scrapy.pipelines.files import FilesPipeline
import os
from urllib.parse import urlparse


class ScrapeDataPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return os.path.basename(urlparse(request.url).path)

    def item_completed(self, results, item, info):
        with open('downloaded.txt', 'a') as f:
            f.write(f'{results[0][1]["path"]}\n')

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from cgitb import text
import scrapy


# item是一个数据结构, 定义一个数据结构, 用于爬取的数据按定义的item结构存储
class TutorialItem(scrapy.Item):  # 继承scrapy.Item
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.self.fail('message')
    pass

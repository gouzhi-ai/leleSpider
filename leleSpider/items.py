# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SymbolabItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    question = scrapy.Field()
    answer = scrapy.Field()
    explain = scrapy.Field()
    url = scrapy.Field()
    subject = scrapy.Field()
    pass

class ThecorestandardsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()
    text = scrapy.Field()
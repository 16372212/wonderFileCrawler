# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FinanceCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PbcPolicyItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    content = scrapy.Field()
    link = scrapy.Field()


class EastMoneyFundItem(scrapy.Item):
    fund_name = scrapy.Field()
    fund_code = scrapy.Field()
    net_value = scrapy.Field()
    # ... 其他你想保存的字段
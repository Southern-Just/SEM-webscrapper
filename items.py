# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NseScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
from scrapy.item import Item, Field


class NseScraperItem(Item):
   # define the fields for your item here like:
   ticker_symbol = Field()
   stock_name = Field()
   stock_price = Field()
   stock_change = Field()
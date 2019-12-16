# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Books_name = scrapy.Field()
    Books_year = scrapy.Field()
    Books_pages = scrapy.Field()
    Books_lng = scrapy.Field()
    Books_desc = scrapy.Field()


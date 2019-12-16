# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from ..items import BooksItem
from scrapy.linkextractors import LinkExtractor


class BookSpider(CrawlSpider):
    name = 'Book'
    #allowed_domains = ['allitbooks.org']
    start_urls = ['http://www.allitebooks.org/web-development/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h2[@class='entry-title']//a"), callback='parse_item', follow=False),
        Rule(LinkExtractor(restrict_xpaths="//link[@rel='next']", tags=('a', 'link', 'area')), callback='parse_item', follow=True),

    )
    link = 0

    def parse_item(self, response):
        item = BooksItem()
        Books_name = response.xpath("//h1[@class='single-title']/text()").extract()
        Books_year = response.xpath("//div[@class='book-detail']/dl/dd[1]/a/text()").extract()
        Books_pages = response.xpath("//div[@class='book-detail']/dl/dd[4]/text()").extract()
        Books_lng = response.xpath("//div[@class='book-detail']/dl/dd[5]/text()").extract()
        Books_desc = response.xpath("//div[@class='entry-content']/p/text()").extract()

        item["Books_name"] = Books_name
        item["Books_year"] = Books_year
        item["Books_pages"] = Books_pages
        item["Books_lng"] = Books_lng
        item["Books_desc"] = Books_desc

        yield item

        # for x in range(5):
        #     self.link = self.link + 1
        #     if self.link == 5:
        #         print(self.link)






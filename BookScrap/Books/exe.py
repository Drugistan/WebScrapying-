from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'Book', '-o', 'output.json'])
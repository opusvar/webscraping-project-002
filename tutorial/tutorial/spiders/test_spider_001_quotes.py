import scrapy


class TestSpider001QuotesSpider(scrapy.Spider):
    name = 'test-spider-001-quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        pass

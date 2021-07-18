import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" #identifies the spider, must be unique in the project
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response): # parsing logic for the response and data capture.  set this to be JSON, text, or XML
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }
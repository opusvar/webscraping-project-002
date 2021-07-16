import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes" #identifies the spider, must be unique in the project

    def start_requests(self): #function that returns an iterable (list or generator), starts the chain of requests
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response): # parsing logic for the response and data capture.  set this to be JSON, text, or XML
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
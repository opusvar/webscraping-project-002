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

        next_page = response.css("li.next a::attr(href)").get() # creates an object called next page, focused on a list element with the class next, and finds the attribute href
        if next_page is not None: # if the get returns a resonse
            next_page = response.urljoin(next_page) # update the next_page variable with the new url
            yield scrapy.Request(next_page, callback=self.parse) # yield a generator object that has the new page information
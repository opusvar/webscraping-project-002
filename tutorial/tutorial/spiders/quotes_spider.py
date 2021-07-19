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

        next_page = response.css("li.next a::attr(href)").get() # creates variable called next page, focused on a list element with the class next, and finds the attribute href
        if next_page is not None: # if the get returns a response
            next_page = response.urljoin(next_page) # update the next_page variable with the new absolute url
            yield scrapy.Request(next_page, callback=self.parse) # yield a generator that has the new page information

# alternative ways to move to another page


    # response.follow() with variable

        """
        next_page = response.css('li.next a::attr(href)').get() # creates a variable called next page, focused on a list element with the calss next and find the attribute href
        if next_page is not None: # if the get returns a repsonse
            yield response.follow(next_page, callback=self.parse) # yield a request instance (needs to be called) that has the new page information using a relative url
        """
    # response.follow() with selector instead of variable

        """
        for href in response.css("ul.pager a::attr(href)"):
            yield response.follow(href, callback=self.parse)
        """
    
    # response.follow() with short cut because it's an <a> tag

        """
        for a in response.css("ul.pager a"):
            yield response.follow(a, callback=self.parse
        """

    # response.follow() with multiple instances to follow
        """
        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)
        """

    # shortest response.parse with multiple instances
        """
        yield from response.follow_all(css="ul.pager a", callback=self.parse)
        """
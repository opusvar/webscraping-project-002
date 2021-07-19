import scrapy # import scrapy

class AuthorSpider(scrapy.Spider): # created a scrapy spider named AuthorSpider
    name = 'author' # project unique name for the spider

    start_url = ["http://quotes.toscrape.com/"] # interable that identifies the start of the crawl

    def parse(self, response): # creates an AuthorSpider method that handles the response information from the crawler
        author_page_links = response.css(".author + a") # creates a variable that contains all of the response objects with the CSS class "author" and their <a> tags
        yield from response.follow_all(author_page_links, self.parse_author) # generator to follow all of the links in the CSS .author objects and send those to be paresed

        pagination_links = response.css("li.next a") # sets the parse method to follow any links
        yield from response.follow_all(pagination_links, self.parse) # generator to follow all the pages that are in the CSS next class and run the parse links

    def parse_author(self, response): # creates an AuthorSpider method that collects the author information for each quote. 
        def extract_with_css(query): # creates a helper function with a parameter query to extract and clean up CSS query info
            return response.css(query).get(default="").strip() # return response that will be cleaned and formatted for further packaging
        # yields an dictionary with formatted author information
        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
        }
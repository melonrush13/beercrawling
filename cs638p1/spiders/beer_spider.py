from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor


class BeerSpider(CrawlSpider):
    name = "beers"
    allowed_domains = ["https://untappd.com"]
    start_urls = [
                  'https://untappd.com/search?q=ale'
                  ]
                  
    rules = (
             
             Rule   (SgmlLinkExtractor(allow=(), restrict_xpaths=('//a[@class="button yellow more_search track-click"]')), callback='parse_items', follow=True),

    )


    def parse_items(self, response):
        for beer in response.css('body'):
                yield {
                    'name': response.css('div.name h1::text').extract(),
                    'brewery': response.css('p.brewery a::text').extract(),
                    'abv': response.css('div.details p.abv::text').extract(),
                    'ibu': response.css('div.details p.ibu::text').extract(),
                    'style': response.css('p.style::text').extract(),
                    'rating': response.css('p.rating span.num::text').extract(),
                }




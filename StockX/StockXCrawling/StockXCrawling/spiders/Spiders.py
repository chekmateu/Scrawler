from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SneakersSpider(CrawlSpider):
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'

    name = 'SneakersSpider'
    allowed_domains = ['stockx.com']
    start_urls = ['https://stockx.com']

    rules = (
        Rule(LinkExtractor(allow="/sneakers")),
    )
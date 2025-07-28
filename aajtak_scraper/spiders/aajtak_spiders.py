import scrapy
from urllib.parse import urljoin
from aajtak_scraper.items import NewsItem

SITEMAP = "https://www.aajtak.in/rssfeeds/news-sitemap.xml"

class AajtakSpider(scrapy.Spider):
    name = "aajtak"
   
    allowed_domains = ["aajtak.in"]
    start_urls = [SITEMAP]

    def parse(self, response):
        for loc in response.xpath('//*[local-name()="loc"]/text()').getall():
         yield scrapy.Request(loc, callback=self.parse_article)

    def parse_article(self, response):
        item = NewsItem()
        item["title"] = response.css("h1::text").get().strip()
        item["published"] = response.xpath(
            '//meta[@property="article:published_time"]/@content'
        ).get()
        item["url"] = response.url
       # image = response.css("div.main-img img::attr(src)").get() or response.css("div.main-img img::attr(data-src)").get()
       # item["image_urls"] = urljoin(response.url, image) if image else None
        image = response.css("div.main-img img::attr(src)").get()
        if not image or "default.webp" in image:
            image = response.css("div.main-img img::attr(data-src)").get()
        item["image_urls"] = response.urljoin(image) if image else None
        
       # image = response.css("figure img::attr(src)").get()
       #
       # item["image_urls"] = [urljoin(response.url, image)]
       # item["image_link"] = [urljoin(response.url, image)]
        #image_urls = response.xpath('//img/@src').get()
        
        return item

import scrapy

class NewsItem(scrapy.Item):
    title = scrapy.Field()
    published = scrapy.Field()
    url = scrapy.Field()
    #image_link = scrapy.Field()
    image_urls = scrapy.Field()     # image pipeline source
    images = scrapy.Field()         # stored info from ImagesPipeline
    snippet = scrapy.Field()

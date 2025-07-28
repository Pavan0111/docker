BOT_NAME = 'aajtak_scraper'
SPIDER_MODULES = ['aajtak_scraper.spiders']
NEWSPIDER_MODULE = 'aajtak_scraper.spiders'


ITEM_PIPELINES = {
    'aajtak_scraper.pipelines.AajtakImages': 200,
    'aajtak_scraper.pipelines.CsvExportPipeline': 300,
}
FEED_EXPORT_ENCODING = "utf-8"
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 1        # keep server happy
IMAGES_EXPIRES = 30       # days

FEEDS = {
    'news_data.csv': {
        'format': 'csv',      # can also be 'json', 'jsonlines', 'jl'
        'fields': [           # specify the exact fields and order
            'image_urls',
            'published',
            'title',
            'url'
        ],
        'encoding': 'utf8',
        'store_empty': False,
        'overwrite': True
    }
}
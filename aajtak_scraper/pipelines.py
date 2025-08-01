from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import CsvItemExporter

class AajtakImages(ImagesPipeline):
    IMAGES_STORE = "images"   # folder at project root

class CsvExportPipeline:
    def open_spider(self, spider):
        self.file = open("aajtak_news.csv", "wb")
        self.exporter = CsvItemExporter(self.file, encoding="utf-8")
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

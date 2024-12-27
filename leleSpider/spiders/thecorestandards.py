import scrapy


class ThecorestandardsSpider(scrapy.Spider):
    name = "thecorestandards"
    allowed_domains = ["www.thecorestandards.org"]
    # start_urls = ["https://www.thecorestandards.org/"]

    def start_requests(self):
        print()

    def parse(self, response):
        pass

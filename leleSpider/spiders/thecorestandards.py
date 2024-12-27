import scrapy


class ThecorestandardsSpider(scrapy.Spider):
    name = "thecorestandards"
    allowed_domains = ["www.thecorestandards.org"]
    start_urls = ['https://www.thecorestandards.org/Math/']
    # start_urls = ['https://www.thecorestandards.org/Math/', 'https://www.thecorestandards.org/ELA-Literacy/']

    def parse(self, response):
        # 提取列表页
        yield scrapy.Request(url=response.url,callback=self.parse_details)

        pass

    def parse_details(self, response):
        # 提取详情页
        self.logger.info(response.url+"  syh20241227")
        pass

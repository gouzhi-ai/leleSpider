import scrapy


class QuestionaiSpider(scrapy.Spider):
    name = "questionai"
    allowed_domains = ["www.questionai.com"]
    start_urls = ["https://www.questionai.com"]

    def parse(self, response):
        pass

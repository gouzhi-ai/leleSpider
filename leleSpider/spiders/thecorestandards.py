import scrapy
from leleSpider.items import ThecorestandardsItem
from bs4 import BeautifulSoup
import re
from markdownify import MarkdownConverter


class ThecorestandardsSpider(scrapy.Spider):
    name = "thecorestandards"
    allowed_domains = ["www.thecorestandards.org"]
    start_urls = ['https://www.thecorestandards.org/ELA-Literacy/']

    # start_urls = ['https://www.thecorestandards.org/Math/', 'https://www.thecorestandards.org/ELA-Literacy/']

    def parse(self, response):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "cache-control": "no-cache",
            "cookie": "_ga=GA1.1.1323559991.1733383172; _ga_XBD2XMMDZB=GS1.1.1735278295.10.1.1735279463.0.0.0",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "referer": "https://www.thecorestandards.org/Math/",
            "sec-ch-ua": "\\Microsoft",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\\Windows",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0"
        }
        # 提取列表页
        yield scrapy.Request(url=response.url, callback=self.parse_details, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        sidebar = soup.find(id="sidebar")
        hrefs = [a['href'] for a in sidebar.find_all('a', href=True)]

        for href in hrefs:
            url = response.urljoin(href)
            yield scrapy.Request(url=url, callback=self.parse_details, headers=headers)
        pass

    def parse_details(self, response):
        # 提取详情页
        item = ThecorestandardsItem()
        item['url'] = response.url

        item['subject'] = "Math"
        match = re.search(r'org/(.*?)/', response.url)
        if match:
            extracted = match.group(1)
            item['subject'] = extracted

        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(class_="article-header")
        item['title'] = title.find("h1").get_text()

        article = soup.find('article')

        item['text'] = "Not found page!"
        if article:
            item['text'] = MarkdownConverter().convert_soup(article)

        yield item
        pass

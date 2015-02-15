import scrapy

class LiveMixTapesSpider(scrapy.Spider):
    name = "livemixtapes.com"
    allowed_domains = ["livemixtapes.com"]
    start_urls = [
        "http://www.livemixtapes.com/main.php",
        "http://www.livemixtapes.com/main.php?show=new"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)

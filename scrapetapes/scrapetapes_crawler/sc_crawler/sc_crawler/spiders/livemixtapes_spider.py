import scrapy


from sc_crawler.items import ScCrawlerItem

class LiveMixTapesSpider(scrapy.Spider):
    name = "livemixtapes.com"
    allowed_domains = ["livemixtapes.com"]
    start_urls = [
        "http://www.livemixtapes.com/main.php",
        "http://www.livemixtapes.com/main.php?show=new"
    ]

    def parse(self, response):
        for sel in response.xpath('//*[@id="content"]/div[3]/div[@class="mixtape_container"]'):
            item = ScCrawlerItem()
            item['artist_name'] = sel.xpath('div[@class="mixtape_djs"]/a/text()').extract()
            item['mixtape_title'] = sel.xpath('div[@class="mixtape_title"]/span/a/text()').extract()
            item['link'] = sel.xpath('div[@class="mixtape_title"]/span/a/@href').extract()
            yield item

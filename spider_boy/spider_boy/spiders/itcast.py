import scrapy


# name = //div[@class="main_mask"]/h2
# time = //div[@class="main_mask"]/h3
# describe = //div[@class="main_mask"]/p

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):
        pass

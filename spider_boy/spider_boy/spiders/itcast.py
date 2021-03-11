import scrapy


# time = //div[@class="masonry_date_block"]
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com']

    def parse(self, response):
        # name = response.xpath('//div[@class="masonry_title_block"')
        print('#' * 30)
        print(type(response))
        print('#' * 30)

import scrapy


# time = //div[@class="masonry_date_block"]
class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['netflav.com']
    start_urls = ['http://netflav.com/all']

    def parse(self, response):
        # name = response.xpath('//div')
        name = response.xpath('//div[@class="masonry_title_block"]')
        print('#' * 30)
        # print(type(response))
        # print(type(name))
        # print(response.text)
        print(name)
        print('#' * 30)

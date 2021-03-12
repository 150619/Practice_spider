import scrapy


class AItcastSpider(scrapy.Spider):
    name = '_itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clears"]')
        print(li_list)

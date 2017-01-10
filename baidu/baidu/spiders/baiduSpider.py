# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# coding:utf-8
import scrapy
from baidu.items import BaiduItem

class Baiduspider(scrapy.Spider):

    #爬虫baidu
    name = 'baidu'

    #允许爬取的页面
    allowed_domains = 'baike.baidu.com'

    #爬虫起始页面.
    start_urls = [
        'https://baike.baidu.com/fenlei/%E8%AF%9D%E9%A2%98%E4%BA%BA%E7%89%A9',
    ]

    def parse(self, response):
        sites = response.xpath('//div[@class="list"]')
        for site in sites:
            item = BaiduItem()
            base_url = site.xpath('a/@href').extract()
            name = site.xpath('a/text()').extract()
            description = site.xpath('p/text()').extract()
            for urls in base_url:
                url = 'https://baike.baidu.com'+urls
            item['url'] = url
            item['name'] = name
            item['description'] = description
            yield item

        next_page = response.xpath('//a[@id="next"]/@href')
        if next_page:
            url = response.urljoin(next_page[0].extract())
            yield scrapy.Request(url, self.parse, dont_filter=True)


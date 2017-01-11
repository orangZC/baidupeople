# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
# coding:utf-8
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from baidu.items import BaiduItem

class Baiduspider(CrawlSpider):

    #爬虫baidu
    name = 'baidu'

    #允许爬取的页面
    allowed_domains = ['baike.baidu.com', 'http://baike.baidu.com']

    #爬虫起始页面.
    start_urls = [
        'http://baike.baidu.com/item/%E5%88%98%E5%BE%B7%E5%8D%8E/114923',
    ]

    #爬取规则
    rules = [
        Rule(LinkExtractor(allow=(r'http://baike.baidu.com/view',),
                           restrict_xpaths=('//div[@class="main-content"]',)), callback='parse_baike', follow=True),
        Rule(LinkExtractor(allow=(r'http://baike.baidu.com/subview',),
                           restrict_xpaths=('//div[@class="main-content"]',)), callback='parse_baike', follow=True),
    ]

    def parse_baike(self, response):
            item = BaiduItem()
            name = response.xpath('//dd[@class="lemmaWgt-lemmaTitle-title"]/h1/text()').extract()
            description = response.xpath('//div[@class="lemma-summary"]')
            des = description[0].xpath('string(.)').extract()[0]
            item['name'] = name
            item['description'] = des
            yield item



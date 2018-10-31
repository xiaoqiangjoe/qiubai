# -*- coding: utf-8 -*-
import scrapy


class TextQiubaiSpider(scrapy.Spider):
    name = 'text_qiubai'
    # allowed_domains = ['www.qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    def parse(self, response):
        div_list = response.xpath('//*[@id="content-left"]/div')
        # xpath方法返回的是一个列表，列表是select类型对象
        all_data = []
        for div in div_list:
            # author = div.xpath('./div/a[2]/h2/text()') 这是一个selector对象，解析的时候有两种方法
            '''第一种'''
            # author = div.xpath('./div/a[2]/h2/text()')[0].extract()
            #  extract()可以将selector对象中存储的数据进行解析操作,必须取出‘[0]’之后才可以extract（）
            '''第二种'''
            author = div.xpath('./div/a[2]/h2/text()').extract_first()
            # extract_first()可以将selector对象中第一个列表元素进行extract,确保有一个值 就用

            content = div.xpath('./a/div/span/text()').extract_first()
            print(content)

            dict ={
                'author':author,
                'content':content
            }
            all_data.append(dict)

        return all_data
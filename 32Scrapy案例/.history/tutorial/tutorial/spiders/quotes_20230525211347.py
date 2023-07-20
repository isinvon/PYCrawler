from cgitb import text
from django.forms import Input
import scrapy



class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]  # allowed_domain是过滤爬取的域名
    """ 在插件OffsiteMiddleware启用的情况下
        （默认是启用的),不在此允许范围内的
        域名就会被过滤,而不会进行爬取，"""
    # start_urls = ["http://quotes.toscrape.com/"]
    start_urls = ["http://quotes.toscrape.com/page/1/"]

    def parse(self, response):  # 分析
        for quote in response.xpath("//div[@class='quote']"):
            # yield{
            #     'text': quote.xpath('./span[@class="text"]/text()').get(),
            #     'author': quote.xpath("./span/small[@class='author']/text()").get(),
            #     'tags': quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()
            # }
            # 或者: 
            text = quote.xpath('./span[@class="text"]/text()').get(),
            author = quote.xpath("./span/small[@class='author']/text()").get(),
            tags = quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()
            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }
            """
            理解yield的含义: 
            yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
            yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值
            重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
            简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始 
            """


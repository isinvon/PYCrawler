from cgitb import text
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]  # allowed_domain是过滤爬取的域名
    """ 在插件OffsiteMiddleware启用的情况下
        (默认是启用的),不在此允许范围内的
        域名就会被过滤,而不会进行爬取，"""
    # start_urls = ["http://quotes.toscrape.com/"]
    start_urls = ["http://quotes.toscrape.com/page/1/"]

    '''这个 parse() 方法来处理这些URL的每个请求，即使我们还没有显式地告诉Scrapy这样做。发生这种情况是因为 parse() 是Scrapy的默认回调方法，在没有显式分配回调的情况下为请求调用该方法。'''
    # 在请求start_urls的时候会返回一个response
    def parse(self, response):  # 解析
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
            # xpath的教程参考'https://www.runoob.com/xpath/xpath-syntax.html'
            yield {
                "text": text,
                "author": author,
                "tags": tags,
            }
            然后终端可以执行
            """
            理解yield的含义: 
            yield 的函数不再是一个普通函数，而是一个生成器generator，可用于迭代
            yield 是一个类似 return 的关键字，迭代一次遇到yield时就返回yield后面(右边)的值
            重点是：下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行
            简要理解：yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始 


            scrapy框架会根据 yield 返回的实例类型来执行不同的操作：
            返回 scrapy.Request 对象，scrapy框架会去获得该对象指向的链接并在请求完成后调用该对象的回调函数。
            返回 scrapy.Item 对象，scrapy框架会将这个对象传递给 pipelines.py做进一步处理。
            """

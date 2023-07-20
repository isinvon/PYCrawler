from django.forms import Input
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/page/1/"]

    def parse(self, response):  # 分析
        for quote in response.xpath("//div[@class='quote']"):

            # yield{
            #     'text': quote.xpath('./span[@class="text"]/text()').get(),
            #     'author': quote.xpath("./span/small[@class='author']/text()").get(),
            #     'tags': quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()
            # }
            text = quote.xpath('./span[@class="text"]/text()').get(),
            author = quote.xpath("./span/small[@class='author']/text()").get(),
            tags = quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()

import scrapy
class ArticleSpider(scrapy.Spider):
    name = 'article'
    start_urls = ['https://www.example.com/articles']
    def parse(self, response):
        for article in response.css('article'):
            yield {
                'title': article.css('h2::text').get(),
                'link': article.css('a::attr(href)').get(),
            }
            next_page = response.css('a.next-page::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

if __name__ == '__main__':
    ArticleSpider()


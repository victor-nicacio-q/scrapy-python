import scrapy

class main_spider(scrapy.Spider):
    name = 'main_spider'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        self.log('Estou aqui: {}'.format(response.url))
        texts = response.xpath('//span[@class="text"]/text()').extract()

        for text in texts:
            yield{
                'text': text
            }

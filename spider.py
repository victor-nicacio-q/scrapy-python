import scrapy
from scrapy.exceptions import CloseSpider

class mainSpider(scrapy.Spider):
    name = 'mainSpider'
    start_urls = ['https://gitlab.com/users/sign_in']

    def parse(self, response):
        self.log('Estou aqui: {}'.format(response.url))

        token = response.css('input[name="authenticity_token"]::attr(value)').extract_first()

        yield scrapy.FormRequest(
                url='https://gitlab.com/users/sign_in',
                formdata={
                    'user[login]': 'victor.nicacio@progmedia.com.br',
                    'user[password]': 'qw3r7yu10p',
                    'authenticity_token': token,
                },
                callback = self.parse_author,
            )

    def parse_author(self, response):

        has_logout = response.css('a[class="sign-out-link"]').extract_first()

        if not has_logout:
            raise CloseSpider('falha no login')
        self.log('login sucedido')

        repos = response.css('span[class="project-name"]').extract()

        for repo in repos:
            yield{
                'Repositorio': repo
            }
import scrapy


class ProgramacaoSpider(scrapy.Spider):
    name = "programacao"
    start_urls = [
        'http://redeglobo.globo.com/programacao.html',
    ]

    def parse(self, response):
        for prog in response.css('section'):
            yield {
                'time': prog.xpath('normalize-space(.//time/text())').extract_first(),
                'programa': prog.xpath('normalize-space(.//h2/text())').extract_first(),
            }




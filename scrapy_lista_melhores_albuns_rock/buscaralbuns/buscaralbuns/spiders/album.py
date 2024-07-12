'''import scrapy


class albumSpider(scrapy.Spider):
    name = "album"
    #allowed_domains = ["exemple.com"]
    start_urls = ('https://pt.wikipedia.org/wiki/Lista_dos_200_%C3%A1lbuns_definitivos_no_Rock_and_Roll_Hall_of_Fame')

    def parse(self, response):
        for disco in response.css('table.wikitable tr'):
            posicao = disco.css('td:nth-child(1) a::text').get()
            album = disco.css('td:nth-child(2)::text').get()
            artista = disco.css('td:nth-child(3) a::text').get()
            data = disco.css('td:nth-child(4) a::text').get()
     
            yield {
                'posicao':posicao,
                'album': album,
                'artista': artista, 
                'data': data
            }
        '''

import scrapy

class WSpider(scrapy.Spider):
    name = 'album'
    start_urls = ['https://pt.wikipedia.org/wiki/Lista_dos_200_%C3%A1lbuns_definitivos_no_Rock_and_Roll_Hall_of_Fame']

    def parse(self, response):
        # Use o SelectorGadget para identificar os seletores CSS dos elementos que contêm os dados que você deseja extrair
        # Neste exemplo, usamos os seletores CSS para os elementos <table> e <tr> que contêm os dados dos álbuns
        for row in response.css('table.wikitable tr')[1:201]:
            # Loop pelas linhas da tabela e extrair os dados
            posicao = row.css('td:nth-child(1) b::text').get()
            album = row.css('td:nth-child(2) a::text').get()
            artista = row.css('td:nth-child(3) a::text').get()
            data_lancamento = row.css('td:nth-child(4) ::text').get().strip().replace('"', '')

            # Usar yield para retornar os dados como um dicionário
            yield {
                'posicao': posicao,
                'album': album,
                'artista': artista,
                'data_lancamento': data_lancamento

            }


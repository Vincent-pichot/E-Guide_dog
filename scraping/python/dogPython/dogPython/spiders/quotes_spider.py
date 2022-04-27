import scrapy

def writeStrInFile(filename, tabList):
    with open(filename, 'w') as f:
        for tab in tabList:
            f.write(tab + "\n")

class fullSpider(scrapy.Spider):
    name = "full"

    def start_requests(self):
        yield scrapy.Request(f'{self.link}', callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{self.name}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

# class tabiSpider(scrapy.Spider):
#     name = "tabi"

#     def start_requests(self):
#         urls = [
#             'https://pass.culture.fr/',
#         ]
#         for url in urls:
#                 yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = f'tabi-{page}.html'
#         tabList = response.xpath('//*[@tabindex]').getall()
#         writeStrInFile(filename, tabList)
#         self.log(f'File {filename} saved')


class argSpider(scrapy.Spider):
    name = "arg"
    
    def start_requests(self):
        self.log(f'Lookig for all {self.container} in {self.link}')
        yield scrapy.Request(f'{self.link}', callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{self.name}.html'
        tabList = response.xpath(f"//{self.container}").getall()
        writeStrInFile(filename, tabList)
        self.log(f'File {filename} saved')
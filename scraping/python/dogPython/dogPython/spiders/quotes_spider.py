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

class fullSplitSpider(scrapy.Spider):
    name = "fullSplit"

    def start_requests(self):
        yield scrapy.Request(f'{self.link}', callback=self.parse)
    
    def removeComments(self, tab):
        cleanTab = []

        for line in tab:
            posStart = line.find('<!--')
            posEnd = -1
            ##print("start = " + str(posStart))
            if posStart != -1:
                # check if the comment is one line only
                posEnd = line.find('-->')
                ##print("end = " + str(posEnd))
                if posEnd != -1:
                    rep = line[posStart:posEnd + 3]
                    ##print(rep)
                    line = line.replace(rep, "")

                # removes all the lines until the end of comment
            cleanTab.append(line)
            # no comment to remove
        return cleanTab

    def parse(self, response):
        page = response.url.split("/")[-2]

        # Création du fichier qui contient tout
        filename = f'{self.name}.html'
        with open(filename, 'wb') as f:
            content = response.body.decode("utf-8")
            tab = content.split("\n")
            clean = self.removeComments(tab)
            #for line in clean:
            #    print(line)
            #f.write(response.body)
            writeStrInFile(filename, clean)
        self.log(f'Saved file {filename}')


        # Rename du nom de la file a créer en "file-img.html"
        filename = f'{self.name}-img.html'
        # Récupération d'un tableau contenant toutes les balises img
        tabImg = response.xpath(f"//img").getall()
        # Ecriture du tableau dans le fichier "file-img.html"
        writeStrInFile(filename, tabImg)
        # Ecriture dans les logs que la page a bien été sauvegarder
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise div
        filename = f'{self.name}-div.html'
        tabDiv = response.xpath(f"//div").getall()
        writeStrInFile(filename, tabDiv)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise p
        filename = f'{self.name}-p.html'
        tabP = response.xpath(f"//p").getall()
        writeStrInFile(filename, tabP)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise form
        filename = f'{self.name}-form.html'
        tabForm = response.xpath(f"//form").getall()
        writeStrInFile(filename, tabForm)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise table
        filename = f'{self.name}-table.html'
        tabTable = response.xpath(f"//table").getall()
        writeStrInFile(filename, tabTable)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise ul
        filename = f'{self.name}-ul.html'
        tabUl = response.xpath(f"//ul").getall()
        writeStrInFile(filename, tabUl)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise input
        filename = f'{self.name}-input.html'
        tabInput = response.xpath(f"//input").getall()
        writeStrInFile(filename, tabInput)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise label
        filename = f'{self.name}-label.html'
        tabLabel = response.xpath(f"//label").getall()
        writeStrInFile(filename, tabLabel)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise span
        filename = f'{self.name}-span.html'
        tabSpan = response.xpath(f"//span").getall()
        writeStrInFile(filename, tabSpan)
        self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise button
        filename = f'{self.name}-button.html'
        tabButton = response.xpath(f"//button").getall()
        writeStrInFile(filename, tabButton)
        self.log(f'File {filename} saved')

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
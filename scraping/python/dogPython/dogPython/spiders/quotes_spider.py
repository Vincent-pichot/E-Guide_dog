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
        comment = False

        for line in tab:
            posStart = line.find('<!--') # trouve le début du commentaire
            posEnd = line.find('-->') # trouve la fin du commentaire
            if posStart != -1:
                comment = True
                if posEnd != -1:
                    rep = line[posStart:posEnd + 3]
                    line = line.replace(rep, "") # supprime un commentaire d'une seule ligne
                    comment = False
                else:
                    line = line.replace(line[posStart:], "") # supprime le début du commentaire sur plusieurs lignes
            elif posEnd != -1 and comment:
                line = line.replace(line[:posEnd + 3], "") # supprime la fin du commentaire sur plusieurs lignes
                comment = False
            elif comment:
                line = line.replace(line, "") # supprime les lignes du commentaire sur plusieurs lignes
            cleanTab.append(line)
        return cleanTab

    def parse(self, response):
        page = response.url.split("/")[-2]

        # Création du fichier qui contient tout
        filename = f'{self.name}.html'
        with open(filename, 'wb') as f:
            content = response.body.decode("utf-8")
            tab = content.split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
        self.log(f'Saved file {filename}')


        # Rename du nom de la file a créer en "file-img.html"
        filename = f'{self.name}-img.html'
        # Récupération d'un tableau contenant toutes les balises img
        tabImg = response.xpath(f"//img").getall()
        # split des lignes
        if len(tabImg) != 0:
            tab = tabImg[0].split("\n")
            # suppression des commentaires
            clean = self.removeComments(tab)
            # Ecriture du tableau dans le fichier "file-img.html"
            writeStrInFile(filename, clean)
            # Ecriture dans les logs que la page a bien été sauvegarder
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise div
        filename = f'{self.name}-div.html'
        tabDiv = response.xpath(f"//div").getall()
        if len(tabDiv) != 0:
            tab = tabDiv[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise p
        filename = f'{self.name}-p.html'
        tabP = response.xpath(f"//p").getall()
        if len(tabP) != 0:
            tab = tabP[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise form
        filename = f'{self.name}-form.html'
        tabForm = response.xpath(f"//form").getall()
        if len(tabForm) != 0:
            tab = tabForm[0].split("\n")
            clean = self.removeComments(tab) 
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise table
        filename = f'{self.name}-table.html'
        tabTable = response.xpath(f"//table").getall()
        if len(tabTable) != 0:
            tab = tabTable[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise ul
        filename = f'{self.name}-ul.html'
        tabUl = response.xpath(f"//ul").getall()
        if len(tabUl) != 0:
            tab = tabUl[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise input
        filename = f'{self.name}-input.html'
        tabInput = response.xpath(f"//input").getall()
        if len(tabInput) != 0:
            tab = tabInput[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise label
        filename = f'{self.name}-label.html'
        tabLabel = response.xpath(f"//label").getall()
        if len(tabLabel) != 0:
            tab = tabLabel[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise span
        filename = f'{self.name}-span.html'
        tabSpan = response.xpath(f"//span").getall()
        if len(tabSpan) != 0:
            tab = tabSpan[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
            self.log(f'File {filename} saved')

        # Même processus qu'au dessus pour la balise button
        filename = f'{self.name}-button.html'
        tabButton = response.xpath(f"//button").getall()
        if len(tabButton) != 0:
            tab = tabButton[0].split("\n")
            clean = self.removeComments(tab)
            writeStrInFile(filename, clean)
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
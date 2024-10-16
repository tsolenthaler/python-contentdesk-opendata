from akeneo.akeneo import Akeneo

class Extraction:
    def __init__(self, host, clientid, secret, user, passwd):
        self.host = host
        self.clientid = clientid
        self.secret = secret
        self.user = user
        self.passwd = passwd
        self.produccts = self.getProducts(self)
        
    def getProducts(self):
        target = Akeneo(self.host, self.clientid, self.secret, self.user, self.passwd)
        search = '{"completeness":[{"operator":"=","value":100,"scope":"ecommerce"}],"enabled":[{"operator":"=","value":true}],"license":[{"operator":"IN","value":["cc0","ccby","ccbync","ccbynd","ccbysa","ccbyncnd","ccbyncsa"]}]}'
        products = target.getProducts(search)
        return products
    
    def createMd(self):
        file = open("products.md", "w")
        for product in self.products:
            file.write("## " + product["identifier"] + "\n")
            file.write("### Description\n")
            file.write(product["description"]["en_US"] + "\n")
            file.write("### Categories\n")
            for category in product["categories"]:
                file.write(category + "\n")
            file.write("### Attributes\n")
            for attribute in product["values"]:
                file.write(attribute + ": " + product["values"][attribute]["en_US"] + "\n")
            file.write("\n")
        return file
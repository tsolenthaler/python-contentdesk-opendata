from contentdeskopendata.extract.extract import Extraction
from contentdeskopendata.transform.transform import Transform
from contentdeskopendata.load.load import Load

class ContentdeskOpenData:
    """
    ContentdeskOpenData class to extract data from a given target and generate a markdown file.
    """
    def __init__(self, host, clientid, secret, user, passwd, cdnurl, path):
        print("INIT - ContentdeskOpenData")
        self.host = host
        self.clientid = clientid
        self.secret = secret
        self.user = user
        self.passwd = passwd
        self.cdnurl = cdnurl
        self.path = path
        self.extractProducts = Extraction(self.host, self.clientid, self.secret, self.user, self.passwd)
        self.debugExtractProducts()
        self.transformProducts = Transform(self.extractProducts.getProducts(), self.cdnurl)
        self.debugTransformProducts()
        self.loadProducts = Load(self.transformProducts.getTransformProducts(), self.path)
        self.debugLoadProducts()
    
    def getExtractProducts(self):
        """
        Returns the extracted products.
        """
        return self.extractProducts
    
    def getTransformProducts(self):
        return self.transformProducts
    
    def getLoadProducts(self):
        return self.loadProducts
    
    def debugExtractProducts(self):
        Load.debugToFile(self.extractProducts.getProducts(), "extractProducts", self.path)
        print("Debug file extractProducts created")
    
    def debugTransformProducts(self):
        Load.debugToFile(self.transformProducts.getTransformProducts(), "transformProducts", self.path)
        print("Debug file transformProducts created")
        
    def debugLoadProducts(self):
        Load.debugToFile(self.loadProducts.getLoadProducts(), "loadProducts", self.path)
        print("Debug file loadProducts created")
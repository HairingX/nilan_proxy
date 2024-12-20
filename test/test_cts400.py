import unittest
from common import NilanProxyCTS400
from modelTester import modelTester

class CTS400Test(modelTester):    
    def setUp(self):
        self.loadedModel = NilanProxyCTS400()
        self.expectedName = "CTS 400"
        self.expectedManufacturer = "Nilan"

if __name__ == '__main__':
    unittest.main()
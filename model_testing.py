import unittest
#from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HomePageTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
if __name__=='__main__':
    unittest.main(verbosity=2)
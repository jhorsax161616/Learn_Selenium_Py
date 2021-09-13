import unittest
from selenium import webdriver
import selenium
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../chromedriver')
        return super().setUpClass()
    
    def test_search(self):
        google = GooglePage(self.driver)
        google.open()
        google.search('Platzi')

        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        return super().tearDownClass()

if __name__=="__main__":
    unittest.main(verbosity = 2)
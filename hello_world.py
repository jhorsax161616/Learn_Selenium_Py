import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')
    
    def test_visit_wikipedia(self):
        self.driver.get('https:///www.wikipedia.org')
    
    def test_my_blog(self):
        self.driver.get('https://orange-moss-01d2a1710.azurestaticapps.net/')
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output= 'reportes', report_name= 'hello_wor_report'))

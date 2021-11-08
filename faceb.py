from re import search
import unittest
from selenium import webdriver
from time import sleep

class FacebTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://www.facebook.com/')
        driver.maximize_window()
        return super().setUp()

    def test_face(self):
        driver = self.driver

        id = driver.find_element_by_name('email')
        passw = driver.find_element_by_name('pass')

        id.send_keys('951590822')
        passw.send_keys('juan318.-190295')
        driver.find_element_by_name('login').click()
        sleep(8)
        
        friends = driver.find_element_by_xpath('//*[@id="mount_0_0_b0"]/div/div[1]/div/div[2]/div[3]/div/div[1]/div[1]/ul/li[2]/span')
        friends.click()
        sleep(3)
        

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElement(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Disappearing Elements').click()
        return super().setUp()
    
    def test_dynamic_elements(self):
        driver = self.driver
        
        self.assertTrue('disappearing_elements'in driver.current_url)
        intentos = 0
        while True:
            intentos += 1
            gallery = driver.find_element_by_class_name('example')
            elements = gallery.find_elements_by_tag_name('a')
            if len(elements) == 4:
                driver.refresh()
            else:
                break
        print(f"Numero de intentos = {intentos}")

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
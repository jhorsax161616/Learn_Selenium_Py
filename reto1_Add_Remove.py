import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElement(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()
        return super().setUp()
    
    def test_Add_Remove_Element(self):
        driver = self.driver
        #comprobando que estamos en la seccion de add_remove
        self.assertTrue('add_remove_elements'in driver.current_url)

        button_add = driver.find_element_by_xpath('//*[@id="content"]/div/button')
        
        for i in range (3):
            for x in range (3):
                button_add.click()
                sleep(1)
            
            button_remove = driver.find_element_by_class_name('added-manually')
            button_remove.click()
            sleep(1)
        
                
    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()


if __name__=='__main__':
    unittest.main(verbosity = 2)

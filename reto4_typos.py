import unittest
from selenium import webdriver

class AddRemoveElement(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()
        return super().setUp()

    def test_Typos(self):
        driver = self.driver
        self.assertTrue('typos'in driver.current_url)
        
        #identificando la etiqueta
        paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
        #haciendo referencia al texto dentro de la etiqueta
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        #variables de control
        tries = 1
        found = False
        correct_tex = "Sometimes you'll see a typo, other times you won't."

        while not found:
            if text_to_check == correct_tex:
                found = True
            else:
                tries += 1
                driver.refresh()
                paragraph_to_check = driver.find_element_by_xpath('//*[@id="content"]/div/p[2]')
                text_to_check = paragraph_to_check.text
        
        self.assertEqual(found, True)
        print(f"It took {tries} tries to find the typo")


    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
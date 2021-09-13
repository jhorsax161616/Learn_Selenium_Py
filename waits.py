import unittest
from selenium import webdriver
#Nos ayuda a hacer referencia a un elemento de la web a travez de sus selectores para interactuar
from selenium.webdriver.common.by import By
#Para hacer de las expected contions y las esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ExplicitWaitTests(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        self.driver.get('http://demo-store.seleniumacademy.com')
        return super().setUp()
    
    
    def test_accout_link(self):
        #esperara maximo 10 segundos hasta que se cumpla la condicion __ get_atrribute optenemos cuantos elementos hay en total
        len = WebDriverWait(self.driver, 3).until(lambda s: s.find_element_by_id('select-language') == '3')

        #Hacer referencia al enlace donde estan las cuentas
        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()


    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        crate_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        crate_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))


    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__ == '__main__':
    unittest.main(verbosity = 2)
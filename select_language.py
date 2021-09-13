import unittest
from selenium import webdriver
#para poder manipular un dropdown nececitamos importar lo siguiente
from selenium.webdriver.support.ui import Select


class LanguageOptions(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path= './chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
        return super().setUp()
    
    def test_select_language(self):
        #opciones de lenguage que queremos validar, sacado de la pagina
        exp_options = ['English', 'French', 'German']
        #almacenando las opciones que nos retorna la consulta
        act_options = []

        #Para poder acceder a las opciones del dropdown pasandolo por medio de find
        select_language = Select(self.driver.find_element_by_id('select-language'))

        #validando que el dropdown tenga 3 opciones
        self.assertEqual(3, len(select_language.options))

        #iterando por cada una de las opciones que tiene el dropd
        for option in select_language.options:
            act_options.append(option.text)
        
        #verificando que la lista de opciones atrapadas sean iguales que las que queremos validar
        self.assertListEqual(exp_options, act_options) #ListEqual compara listas

        #verificando que la palabra English sea la que aparece en ele droD 
        # podria ser tambien como el lenguage seleccionado por defecto??? 
        self.assertEqual('English', select_language.first_selected_option.text)

        #seleccionando el idioma Aleman
        select_language.select_by_visible_text('German')

        #verificando que realmente se este en Aleman por medio de url
        self.assertTrue('store=german' in self.driver.current_url)

        #Eligiendo un idioma a travez de indice
        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self) -> None:
        self.driver.implicitly_wait(3)
        self.driver.close()
        return super().tearDown()


if __name__ == '__main__':
    unittest.main(verbosity = 2)
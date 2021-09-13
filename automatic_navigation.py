import unittest
from selenium import webdriver
#para poder incluir pausas podemos usar lo siguiente pero no es recomendable
from time import sleep

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('https://google.com')
        return super().setUp()
    
    def test_browser_navigation(self):
        driver = self.driver

        #asignamos el buscador con find a la variable
        search_field = driver.find_element_by_name('q')

        #limpiar lo que hay ahi como buema practica
        search_field.clear()

        #enviando termino de busqueda que queremos
        search_field.send_keys('platzi')
        #lo subimos o como dar click a buscar
        search_field.submit()

        #retroceder de pagina
        driver.back()
        #pausa no recomendable
        sleep(3)
        #avanzar a pagina adelante
        driver.forward()
        sleep(3)
        #refrescar la pagina
        driver.refresh()
        sleep(3)

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
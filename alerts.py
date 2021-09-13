import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
        return super().setUp()

    def test_compare_products_removal_alert(self):
        driver = self.driver
        #Guardamos en la variable el elemento
        search_field = driver.find_element_by_name('q')

        #Buena practiva limpiar todo lo que se encuentre en la barra de busqueda
        search_field.clear()

        #enviando texto a buscar y lo subimos por el formulario con submit
        search_field.send_keys('tee')
        search_field.submit()

        #buscamos el elemento de add compare y haciendole click
        driver.find_element_by_class_name('link-compare').click()

        #buscando el borrar todo por su link text y dandole click para que salga el alert
        driver.find_element_by_link_text('Clear All').click()

        #Interactuando con el alert mostrado
        #Esto hace un cambio del focus al alert -->  el cursor se encuentra en el alert
        alert = driver.switch_to_alert()

        #extraemos el texto que nos muestra el alert
        alert_text = alert.text

        #Comparamos si es que el texto del alert dice lo que queremos que diga
        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text)

        #simulando click en aceptar
        alert.accept()

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
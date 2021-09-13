import unittest
from ddt import ddt, data, unpack
from selenium import webdriver

@ddt
class searchDDT(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')
        return super().setUp()

    #incluye tuplas con los terminos q' vamos a buscar y cantidad de elementos del resultado
    @data(('dress', 5), ('music', 5))
    #desenpaqueta las tuplas para poder consultarlas individualmente
    @unpack
    
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver

        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()

        products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)
        
        self.assertEqual(expected_count, len(products))

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity=2)
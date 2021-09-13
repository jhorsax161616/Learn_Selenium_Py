import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage(object):
    def __init__(self, driver) -> None:
        self._driver = driver
        self._url = 'https://google.com'
        self.search_locator = 'q'
        super().__init__()
    
    @property
    def is_loader(self):
        WebDriverWait(self._drinver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))

        return True
    
    @property
    def keyword(self):
        input_field = self._driver.find_element_by_name('q')
        return input_field.get_attribute('value')
    
    def open(self):
        self._driver.get(self._url)

    def type_search(self, keyword):
        input_fiel = self._driver.find_element_by_name('q')
        input_fiel.send_keys(keyword)
    
    def click_submit(self):
        input_fiel = self._driver.find_element_by_name('q')
        input_fiel.submit()
    
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()
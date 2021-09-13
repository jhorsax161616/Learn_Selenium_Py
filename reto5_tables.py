import unittest
from selenium import webdriver
from time import sleep

class Tables(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()
        return super().setUp()
    
    def test_data_table(self):
        driver = self.driver
        self.assertTrue('tables'in driver.current_url)

        table_data = [[] for i in range(5)]
        print(table_data)

        for i in range(len(table_data)):
            header = driver.find_element_by_xpath(f'//*[@id="table1"]/thead/tr/th[{i+1}]/span')
            table_data[i].append(header.text)

            for j in range(4):
                row_data = driver.find_element_by_xpath(f'//*[@id="table1"]/tbody/tr[{j+1}]/td[{i+1}]')
                table_data[i].append(row_data.text)
        
        print(table_data)

    def tearDown(self) -> None:
        self.driver.close()
        return super().tearDown()

if __name__=='__main__':
    unittest.main(verbosity = 2)
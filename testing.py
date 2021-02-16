import os
import threading
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

class TestRequest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
      chrome_options = Options()
      chrome_options.add_argument("--headless")
        
      cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        
#a test to ensure google.com is working
    def test_request(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://google.com/ncr")
        self.driver.find_element(By.NAME, "q").send_keys("cheese" + Keys.RETURN)
        first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
        self.assertEqual('Show more', first_result.get_attribute("textContent"))




if __name__ == '__main__':
    unittest.main()
    #print ("all done tests ran" )

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class BookBytePOM:

    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Locators
        self.locator_keywords = "ctl00_ContentPlaceHolder1_tbKeywords"
        self.locator_btn_search = "ctl00_ContentPlaceHolder1_ibSearch"
        self.locator_result_titles = "ctl00_ContentPlaceHolder1_resultsSetGridView_ctl03_aProductLink"
        self.locator_result_count = "//*[@id='ctl00_ContentPlaceHolder1_up']/div/span"

    def go_to_page(self):
        self.driver.get("https://www.bookbyte.com/advancedsearch.aspx")

    @property
    def keywords(self):
        return self.driver.find_element_by_id(self.locator_keywords)

    @property
    def btn_search(self):
        return self.driver.find_element_by_id(self.locator_btn_search)

    @property
    def results(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(presence_of_element_located((By.XPATH, self.locator_result_count)))
        return self.driver.find_elements_by_id(self.locator_result_titles)

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class AmazonPOM:

    def __init__(self, driver: Chrome):
        self.driver = driver

        # Locators
        self.locator_address = "//*[@id='seller-profile-container']/div[2]/div/ul/li[2]/span/ul/li[1]/span"

    def go_to_page(self):
        self.driver.get("https://www.amazon.com/sp?seller=A2N51X1QYGFUPK")

    @property
    def address(self):
        return self.driver.find_element(By.XPATH, self.locator_address)

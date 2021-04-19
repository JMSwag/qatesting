import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import AmazonPOM, BookBytePOM, GoogleBooksAPIClient


class TestUi(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_amazon(self):
        amazon_pom = AmazonPOM(self.driver)
        amazon_pom.go_to_page()
        self.assertEqual("2800 Pringle Rd SE Suite 100", amazon_pom.address.text)

    def test_bookbyte(self):
        bookbyte_pom = BookBytePOM(self.driver)
        bookbyte_pom.go_to_page()

        keyword_search_term = 'college'
        bookbyte_pom.keywords.send_keys(keyword_search_term)
        bookbyte_pom.btn_search.click()

        for result in bookbyte_pom.results:
            self.assertIn(keyword_search_term, result.text.lower())


class TestAPI(unittest.TestCase):

    def test_google_books_api(self):
        client = GoogleBooksAPIClient()

        truth = ["Brian W. Kernighan", "Dennis M. Ritchie"]
        authors = client.authors_by_ibsn('0131103628', "The C Programming Language")
        self.assertEqual(truth, authors)


if __name__ == '__main__':
    unittest.main()
    # print("all done tests ran" )

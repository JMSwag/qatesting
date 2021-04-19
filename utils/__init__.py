import requests

from .poms.amazon import AmazonPOM
from .poms.bookbyte import BookBytePOM


class GoogleBooksAPIClient:

    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/volumes?q="

    def authors_by_ibsn(self, ibsn, title):
        books = requests.get(self.base_url + "isbn+{}".format(ibsn)).json()['items']
        for book in books:
            if book['volumeInfo']['title'] == title:
                return book['volumeInfo']['authors']

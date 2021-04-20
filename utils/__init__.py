import requests

from .poms.amazon import AmazonPOM
from .poms.bookbyte import BookBytePOM


class GoogleBooksAPIClient:

    def __init__(self):
        self.base_url = "https://www.googleapis.com/books/v1/volumes?q="

    def authors_by_ibsn(self, ibsn):
        book = requests.get(self.base_url + "isbn:{}".format(ibsn)).json()['items'][0]
        return book['volumeInfo']['authors']

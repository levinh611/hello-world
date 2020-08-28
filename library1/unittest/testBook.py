import unittest
from librarymanage.models.book import Book
from librarymanage.unittest.data import book1,book2,book3,book4,list1,list2,list3,list4,list5,list6,list7

class TestBook(unittest.TestCase):
    def test_create(self):
        self.assertTrue(Book.createBook(**book1))
        self.assertTrue(Book.createBook(**book2))

    def test_update(self):
        self.assertTrue(Book.updateBook(**book3))
        self.assertTrue(Book.updateBook(**book4))

    def test_delete(self):
        self.assertTrue(Book.deleteBook(2))
        self.assertTrue(Book.deleteBook(5))

    def test_search(self):
        self.assertTrue(Book.search_by_id_book(2))
        self.assertTrue(Book.search_by_id_book(6))

    def test_get_list(self):
        self.assertTrue(Book.get_list_book(**list1))
        self.assertTrue(Book.get_list_book(**list2))
        self.assertTrue(Book.get_list_book(**list3))
        self.assertTrue(Book.get_list_book(**list4))
        self.assertTrue(Book.get_list_book(**list5))
        self.assertTrue(Book.get_list_book(**list6))
        self.assertTrue(Book.get_list_book(**list7))

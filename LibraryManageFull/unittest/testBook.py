import unittest
from librarymanage.models.book import Book
from librarymanage.unittest.data import book1,book2,book3,book4,list1,list2,list3,list4,list5,list6,list7
from librarymanage.connection import library_mysql



class TestBook(unittest.TestCase):
    def test_create_book(self):
        with library_mysql.atomic() as txn:
            Book.createBook(**book1)
            Book.createBook(**book2)
            txn.rollback()



    def test_update_book(cls):
        with library_mysql.atomic() as txn:
            Book.updateBook(**book3)
            Book.updateBook(**book4)
            txn.rollback()


    def test_delete_book(self):
        with library_mysql.atomic() as txn:
            Book.deleteBook(2)
            Book.deleteBook(5)
            txn.rollback()

    def test_search_book(self):
        with library_mysql.atomic() as txn:
            Book.search_by_id_book(2)
            Book.search_by_id_book(6)
            txn.rollback()

    def test_get_list_book(self):
        with library_mysql.atomic() as txn:
            Book.get_list_book(**list1)
            Book.get_list_book(**list2)
            Book.get_list_book(**list3)
            Book.get_list_book(**list4)
            Book.get_list_book(**list5)
            Book.get_list_book(**list6)
            Book.get_list_book(**list7)
            txn.rollback()


from librarymanage.models.borrowbook import Borrowbook
import unittest
from librarymanage.connection import library_mysql
from librarymanage.unittest.data import user1,user15,user14,user13,user12,user11,user10,user9,user7,user6,user5,user4,user3,user2,user8

class TestBorrowbook(unittest.TestCase):
    def test_create(self):
        with library_mysql.atomic() as txn:
            Borrowbook.createInfo(**user12)
            Borrowbook.createInfo(**user13)
            txn.rollback()

    def test_update(self):
        with library_mysql.atomic() as txn:
            Borrowbook.updateInfo(**user14)
            Borrowbook.updateInfo(**user15)
            txn.rollback()
    def test_delete(self):
        with library_mysql.atomic() as txn:
            Borrowbook.deleteInfo(2)
            Borrowbook.deleteInfo(4)
            txn.rollback()

    def test_search(self):
        with library_mysql.atomic() as txn:
            Borrowbook.search(2)
            Borrowbook.search(1)
            txn.rollback()

    def test_get_detail(self):
        with library_mysql.atomic() as txn:
            Borrowbook.get_detail(7)
            Borrowbook.get_detail(10)
            txn.rollback()

    def test_get_list(self):
        with library_mysql.atomic() as txn:
            Borrowbook.get_list(**user1)
            Borrowbook.get_list(**user2)
            Borrowbook.get_list(**user3)
            Borrowbook.get_list(**user4)
            Borrowbook.get_list(**user5)
            Borrowbook.get_list(**user6)
            Borrowbook.get_list(**user7)
            Borrowbook.get_list(**user8)
            Borrowbook.get_list(**user9)
            Borrowbook.get_list(**user10)
            Borrowbook.get_list(**user11)
            txn.rollback()


from librarymanage.models.borrowbook import Borrowbook
import unittest
from librarymanage.unittest.data import user1,user15,user14,user13,user12,user11,user10,user9,user7,user6,user5,user4,user3,user2,user8

class TestBorrowbook(unittest.TestCase):
    def test_create(self):
        self.assertTrue(Borrowbook.createInfo(**user12))
        self.assertTrue(Borrowbook.createInfo(**user13))

    def test_update(self):
        self.assertTrue(Borrowbook.updateInfo(**user14))
        self.assertTrue(Borrowbook.updateInfo(**user15))

    def test_delete(self):
        self.assertTrue(Borrowbook.deleteInfo(2))
        self.assertTrue(Borrowbook.deleteInfo(4))

    def test_search(self):
        self.assertTrue(Borrowbook.search(2))
        self.assertTrue(Borrowbook.search(1))

    def test_get_detail(self):
        self.assertTrue(Borrowbook.get_detail(2))
        self.assertTrue(Borrowbook.get_detail(4))

    def test_get_list(self):
        self.assertTrue(Borrowbook.get_list(**user1))
        self.assertTrue(Borrowbook.get_list(**user2))
        self.assertTrue(Borrowbook.get_list(**user3))
        self.assertTrue(Borrowbook.get_list(**user4))
        self.assertTrue(Borrowbook.get_list(**user5))
        self.assertTrue(Borrowbook.get_list(**user6))
        self.assertTrue(Borrowbook.get_list(**user7))
        self.assertTrue(Borrowbook.get_list(**user8))
        self.assertTrue(Borrowbook.get_list(**user9))
        self.assertTrue(Borrowbook.get_list(**user10))
        self.assertTrue(Borrowbook.get_list(**user11))
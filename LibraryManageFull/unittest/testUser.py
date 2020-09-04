import unittest
from librarymanage.models.user import User
from librarymanage.unittest.data import User1,User11,User10,User9,User8,User7,User6,User5,User4,User3,User2
from librarymanage.connection import library_mysql

class TestUser(unittest.TestCase):
    def test_create_user(self):
        with library_mysql.atomic() as txn:
            User.createUser(**User1)
            User.createUser(**User2)
            txn.rollback()

    def test_update_user(self):
        with library_mysql.atomic() as txn:
            User.updateUser(**User3)
            User.updateUser(**User4)
            txn.rollback()

    def test_delete_user(self):
        with library_mysql.atomic() as txn:
            User.deleteUser(1)
            User.deleteUser(5)
            txn.rollback()

    def test_search_user(self):
        with library_mysql.atomic() as txn:
            User.search_by_id_user(3)
            User.search_by_id_user(7)
            txn.rollback()
    def test_get_list_user(self):
        with library_mysql.atomic() as txn:
            User.get_list_user(**User5)
            User.get_list_user(**User6)
            User.get_list_user(**User7)
            User.get_list_user(**User8)
            User.get_list_user(**User9)
            User.get_list_user(**User10)
            User.get_list_user(**User11)
            txn.rollback()
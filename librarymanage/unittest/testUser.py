import unittest
from librarymanage.models.user import User
from librarymanage.unittest.data import User1,User11,User10,User9,User8,User7,User6,User5,User4,User3,User2
class TestUser(unittest.TestCase):
    def test_create(self):
        self.assertTrue(User.createUser(**User1))
        self.assertTrue(User.createUser(**User2))

    def test_update(self):
        self.assertTrue(User.updateUser(**User3))
        self.assertTrue(User.updateUser(**User4))

    def test_delete(self):
        self.assertTrue(User.deleteUser(1))
        self.assertTrue(User.deleteUser(5))

    def test_search(self):
        self.assertTrue(User.search_by_id_user(3))
        self.assertTrue(User.search_by_id_user(7))

    def test_get_list(self):
        self.assertTrue(User.get_list_user(**User5))
        self.assertTrue(User.get_list_user(**User6))
        self.assertTrue(User.get_list_user(**User7))
        self.assertTrue(User.get_list_user(**User8))
        self.assertTrue(User.get_list_user(**User9))
        self.assertTrue(User.get_list_user(**User10))
        self.assertTrue(User.get_list_user(**User11))
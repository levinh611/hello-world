from librarymanage.models.borrowbook import Borrowbook
import unittest
#from librarymanage.models.borrowbook import Borrowbook

class TestCreate(unittest.TestCase):
    def test_create(self):
        user1={"id_user":1,
               "id_book":3,
               "date":"2020-12-09",
               "price":45000}
        self.assertTrue(Borrowbook.createInfo(**user1))

    def test_create2(self):
        user2 = {"id_user":5,
                 "id_book":7,
                 "date":"2019-05-17",
                 "price":34000}
        self.assertTrue(Borrowbook.createInfo(**user2))

class TestUpdate(unittest.TestCase):
    def test_update(self):
        user1 = {"id_user":3,
                 "id_book":3,
                 "date":"2019-11-17",
                 "price":23000}
        self.assertTrue(Borrowbook.updateInfo(**user1))
    def test_update2(self):
        user2 = {"id_user":4,
                 "id_book":7,
                 "date":"2020-04-05",
                 "price":45000}
        self.assertTrue(Borrowbook.updateInfo(**user2))

class TestDelete(unittest.TestCase):
    def test_delete(self):
        self.assertTrue(Borrowbook.deleteInfo(2))
    def test_delete2(self):
        self.assertTrue(Borrowbook.deleteInfo(4))

class TestSearch(unittest.TestCase):
    def test_search(self):
        self.assertTrue(Borrowbook.search(2))
    def test_search2(self):
        self.assertTrue(Borrowbook.search(1))

class TestGetDetail(unittest.TestCase):
    def test_get_detail(self):
        self.assertTrue(Borrowbook.get_detail(2))
    def test_get_detail2(self):
        self.assertTrue(Borrowbook.get_detail(4))

class TestGetList(unittest.TestCase):
    def test_get_list(self):
        user1 = {"keyword":"v"}
        self.assertTrue(Borrowbook.get_list(**user1))
    def test_get_list2(self):
        user2 = {"keyword":"v",
                 "page_size":5}
        self.assertTrue(Borrowbook.get_list(**user2))
    def test_get_list3(self):
        user3 = {"keyword":"v",
                 "page_index":3}
        self.assertTrue(Borrowbook.get_list(**user3))
    def test_get_list4(self):
        user4 = {"keyword":"v",
                 "from_price":2000}
        self.assertTrue(Borrowbook.get_list(**user4))
    def test_get_list5(self):
        user5 = {"keyword":"a",
                 "to_price":60000}
        self.assertTrue(Borrowbook.get_list(**user5))
    def test_get_list6(self):
        user6 = {"keyword":"v",
                 "order_field":"price"}
        self.assertTrue(Borrowbook.get_list(**user6))
    def test_get_list7(self):
        user7 = {"keyword":"a",
                 "from_date":"2019-01-01"}
        self.assertTrue(Borrowbook.get_list(**user7))
    def test_get_list8(self):
        user8 = {"keyword":"h",
                 "to_date":"2020-01-01"}
        self.assertTrue(Borrowbook.get_list(**user8))
    def test_get_list9(self):
        user9 = {"keyword":"a",
                 "from_price":2000,
                 "to_price":100000}
        self.assertTrue(Borrowbook.get_list(**user9))
    def test_get_list10(self):
        user10 = {"keyword":"g",
                  "page_size":5,
                  "page_index":1,
                  "from_price":2000,
                  "to_price":100000,
                  "from_date":"2019-01-01",
                  "to_date":"2020-12-22",
                  "order_field":"date"}
        self.assertTrue(Borrowbook.get_list(**user10))
    def test_get_list11(self):
        user11 = {"keyword": "v",
                  "page_size": 3,
                  "page_index": 0,
                  "from_price": 1000,
                  "to_price": 90000,
                  "from_date": "2019-01-08",
                  "to_date": "2019-12-22",
                  "order_field":"price"}
        self.assertTrue(Borrowbook.get_list(**user11))




from librarymanage.models.borrowbook import Borrowbook
a = Borrowbook()
user10 = {"keyword":"g",
                  "page_size":1,
                  "page_index":1,
                  "from_price":2000,
                  "to_price":100000,
                  "from_date":"2019-01-01",
                  "to_date":"2020-12-22",
                  "order_field":"date"}

h = a.get_list(**user10)
print(h)
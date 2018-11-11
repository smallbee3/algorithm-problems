"""
12. Sorting by Price

Implement the function sort_by_price_ascending, which:

* Accepts a string in JSON format, as in the example below.
* Orders items by price in ascending order.
* If two products have the same price, it orders them by their name in alphabetical order.
* Returns a string in JSON format that is equivalent to the one in the input foramt.

For example, the call

Products.sort_by_price_ascending(
  '[{"name":"eggs","price":1},
  {"name":"coffee","price":9.99},
  {"name":"rice","price":4.04}]'
);


should return

'[{"name":"eggs","price":1},
{"name":"rice","price":4.04},
{"name":"coffee","price":9.99}]'

"""

import json


class Products:

    @staticmethod
    def find_min_dict(json_list):

        min_name = json_list[0]['name']
        min_price = json_list[0]['price']
        min_idx = 0

        for idx, dic in enumerate(json_list[1:]):
            if min_price > dic['price']:
                min_price = dic['price']
                min_name = dic['name']
                min_idx = idx + 1

            elif min_price == dic['price']:
                if min_name > dic['name']:
                    min_price = dic['price']
                    min_name = dic['name']
                    min_idx = idx + 1
        return min_idx

    @staticmethod
    def sort_by_price_ascending(json_string):

        json_list = json.loads(json_string)
        for i in range(len(json_list)):
            min_idx = Products.find_min_dict(json_list[i:]) + i
            json_list[i], json_list[min_idx] = json_list[min_idx], json_list[i]
        return str(json_list)


# print(Products.sort_by_price_ascending(
#     '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
# )

print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":4.06},{"name":"rice3","price":4.09}]')
)

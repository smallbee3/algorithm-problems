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


```
import json


class Products:

    @staticmethod
    def sort_by_price_ascending(json_string):
        pass


print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
)

# print(Products.sort_by_price_ascending(
#     '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":4.06},{"name":"rice3","price":4.09}]')
# )
```


* Subject - sorting

* Learning
    1. sorting through two ways
        - Insert into new sorted list (v, prefer)
        - Swapping

    2. read JSON file in python using json function
        - json.loads(<json-string>)
        - json.dumps(<list with dicts>)

"""

# import json
#
#
# class Products:
#
#     @staticmethod
#     def find_min_dict(json_list):
#
#         min_name = json_list[0]['name']
#         min_price = json_list[0]['price']
#         min_idx = 0
#
#         for idx, dic in enumerate(json_list[1:]):
#             if min_price > dic['price']:
#                 min_price = dic['price']
#                 min_name = dic['name']
#                 min_idx = idx + 1
#
#             elif min_price == dic['price']:
#                 if min_name > dic['name']:
#                     min_price = dic['price']
#                     min_name = dic['name']
#                     min_idx = idx + 1
#         return min_idx
#
#     @staticmethod
#     def sort_by_price_ascending(json_string):
#
#         json_list = json.loads(json_string)
#         for i in range(len(json_list)):
#             min_idx = Products.find_min_dict(json_list[i:]) + i
#             json_list[i], json_list[min_idx] = json_list[min_idx], json_list[i]
#         return str(json_list)
#
#
# # print(Products.sort_by_price_ascending(
# #     '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
# # )
#
# print(Products.sort_by_price_ascending(
#     '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":4.06},{"name":"rice3","price":4.09}]')
# )


"""
181112 Review

Time : 13 min
"""


import json


class Products:

    @staticmethod
    def sort_by_price_ascending(json_string):
        json_string = json.loads(json_string)

        sorted_list = [json_string[0]]

        def sorting_product(i, j):
            if i['price'] < j['price']:
                return i
            elif i['price'] > j['price']:
                return j
            else:
                return i if i['name'] > j['name'] else j

        for i in json_string[1:]:
            for idx, j in enumerate(sorted_list):
                if i == sorting_product(i, j):
                    sorted_list.insert(idx, i)
                    break
                if idx == len(sorted_list)-1:
                    sorted_list.insert(idx+1, i)
                    break

        # return str(sorted_list)

        # print(type(json.dumps(sorted_list)))
        # print(sorted_list)
        return json.dumps(sorted_list)


print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
)
print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":4.06},{"name":"rice3","price":4.09}]')
)


"""
181130 Review

Time : 12 min
"""

# 181130
# Nested structure removed in the inner function


class Products:

    @staticmethod
    def sort_by_price_ascending(json_string):

        def compare_price_and_name(dict1, dict2):
            if dict1['price'] < dict2['price']:
                return dict1
            elif dict1['price'] > dict2['price']:
                return dict2

            if dict['name'] < dict2['name']:
                return dict1
            else:
                return dict2

        json_list = json.loads(json_string)

        new_list = [json_list[0]]
        for dict1 in json_list[1:]:

            for idx, dict2 in enumerate(new_list):
                if compare_price_and_name(dict1, dict2) == dict1:
                    new_list.insert(idx, dict1)
                    break
                if idx == len(new_list)-1:
                    new_list.insert(idx+1, dict1)
                    break

        return json.dumps(new_list)


print()
print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
)
print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":4.06},{"name":"rice3","price":4.09}]')
)


import json


class Products:
    @staticmethod
    def sort_by_price_ascending(json_string):
        jlist = json.loads(json_string)
        sorted_list = sorted(jlist, key=lambda k: k['price'])

        return json.dumps(sorted_list)


# print(Products.sort_by_price_ascending(
#     '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]')
# )

print(Products.sort_by_price_ascending(
    '[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04},{"name":"rice2","price":1},{"name":"abc","price":1}]')
)

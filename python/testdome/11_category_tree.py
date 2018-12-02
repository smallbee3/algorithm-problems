"""
11. Category Tree

A category tree is a representation of a set of categories and their
parent-child relationships. Each category has a unique name (no
two categories have the same name). A category can have a parent
category. Categories without a parent category are called root
categories.

To add a category to a category tree, the name and the parent of
the category should be provided. When adding a root category, a
None value should be provided as the parent. A call to get_children
should return an array containing the direct children of the specified
category in any order.

KeyError should be thrown when adding a category that ahs already
been added anywhere in the CategoryTree of if a parent is specified
but does not exist.

For example:

c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A') or []))

Running this code should display 'B,C' or 'C,B'.

Time : (more than) 60 min
Tests : 3 pass ?
    Example case: Correct answer
    Simple case: ?
    KeyError is raised when needed: Correct answer


* Subject - New definition of existing algorithm concept
             (Define Tree with dict not with variable as it used to do)
              e.g. self.left = None, self.right = None (X)
* Learning
    1. The usage of hash table in the complex situation
        (There was a hint of 'hash table' in the problem description,
         which is 'KeyError')

    2. 'Make raise error in your code' could mean I really had to raise an error if it is needed.

"""


class CategoryTree:

    def __init__(self):
        pass

    def add_category(self, category, parent):
        pass

    def get_children(self, parent):
        return []


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
# print(','.join(c.get_children('A') or []))



# class CategoryTree:
#
#     # def __init__(self, name=None, parent=None, chldren=[]):
#     #     # unique name logic
#     #     self.name = name
#     #     self.parent = parent
#     #     self.children = chldren
#
#     def __init__(self):
#         # unique name logic
#         self.root_node = None
#         self.node_dict = {}
#         self.node_list = []
#
#     def add_category(self, category, parent):
#         # KeyError (1.no parent, 2.already added)
#
#         if parent is None:
#             self.root_node = category
#             self.node_dict[category] = []
#             self.node_list.append(category)
#             return
#
#         # KeyError (1) - No parents
#         if parent not in self.node_list:
#             raise KeyError
#
#         if self.node_dict.get(parent):
#             # KeyError (2) - Already exist
#             if category in self.node_dict[parent]:
#                 raise KeyError
#             else:
#                 self.node_dict[parent] += [category]
#                 self.node_list.append(category)
#         else:
#             self.node_dict[parent] = [category]
#             self.node_list.append(category)
#
#         # print(self.node_dict)
#         print(f'node_list : {self.node_list}')
#
#     def get_children(self, parent):
#         if self.node_dict.get(parent):
#             return self.node_dict[parent]
#         else:
#             return []
#
#
# c = CategoryTree()
# c.add_category('A', None)
# c.add_category('B', 'A')
# c.add_category('C', 'A')
#
# # KeyError 1
# # c.add_category('C', 'A')
#
# # KeyError 2
# # c.add_category('D', 'E')
# # c.add_category('D', 'E')
#
# # Simple case
# c.add_category('D', 'C')
# c.add_category('E', 'B')
# c.add_category('G', 'B')
# c.add_category('H', 'B')
# c.add_category('F', 'E')
#
#
# print(','.join(c.get_children('A') or []))
# print(','.join(c.get_children('B') or []))


# 1. Each category has a unique name
# 2. Key Error
#   - when adding already added category
#   - parent does not exist


"""
181112 Review

Time : 18 min
Tests : 1 pass / 2 fail
    Example case: Correct answer
    Simple case: Wrong answer
    KeyError is raised when needed: Wrong answer
"""

# Fail - unique name

# class CategoryTree:
#
#     def __init__(self):
#         self.category_dict = {}
#         self.category_list = []
#
#     def add_category(self, category, parent):
#         if parent is None:
#             self.category_dict[category] = []
#             self.category_list.append(category)
#             return
#
#         if self.category_dict.get(parent):
#             if category not in self.category_dict[parent]:
#                 self.category_dict[parent] += [category]
#                 self.category_list.append(category)
#             else:
#                 raise KeyError('Same category already exists!')
#         elif parent in self.category_list:
#             self.category_dict[parent] = [category]
#             self.category_list.append(category)
#         else:
#             raise KeyError('The parent node does not exist!')
#
#     def get_children(self, path):
#         return self.category_dict[path]


"""
181112 Review

Time : 18 min
Tests : 3 pass ?
Example case: Correct answer
Simple case: ?
KeyError is raised when needed: Correct answer
"""


class CategoryTree:

    def __init__(self):
        self.category_dict = {}

    def add_category(self, category, parent):

        if category in self.category_dict:
            raise KeyError('Same category already exists!')
            # raise KeyError('The parent node already exists!')

        # All node becomes a parent node
        self.category_dict[category] = []

        # if self.category_dict.get(parent):
        if parent is not None:
            self.category_dict[parent] += [category]
        # else:
        #     self.category_dict[parent] = [category]

    def get_children(self, path):
        return self.category_dict[path]


c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')

# KeyError 1 - duplicate
# c.add_category('C', 'A')

# KeyError 2 - no parent
# c.add_category('D', 'E')

# KeyError 3 - unique name
c.add_category('D', 'C')
# c.add_category('D', 'B')

# Simple case
c.add_category('G', 'B')
c.add_category('H', 'B')


print(','.join(c.get_children('A') or []))
print(','.join(c.get_children('B') or []))


"""
181130 Review

Time : 25 min
Tests : 3 pass ?
Example case: Correct answer
Simple case: ?
KeyError is raised when needed: Correct answer
"""

# 181130
# By using the way of early exit, the code becomes more readable.

class CategoryTree:

    def __init__(self):
        # self.name = None
        # self.parent = None
        self.category_dict = {}

    def add_category(self, category, parent):
        # self.name = category
        # self.parent = parent

        # root node
        if parent is None:
            self.category_dict[category] = []
            return

        # KeyError1 - no parents
        if not self.category_dict.get(parent) and self.category_dict.get(parent) != []:
            raise KeyError('Parent does not exist!')

        # KeyError2 - duplicate

        # 181130
        # This code is not enough for unique validation
        # if category in self.category_dict[parent]:
        # ->
        if category in self.category_dict:
            raise KeyError('Category already exists!')

        self.category_dict[parent].append(category)
        self.category_dict[category] = []

    def get_children(self, parent):
        return self.category_dict[parent]


print()
c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')

# KeyError 1 - duplicate
# c.add_category('C', 'A')

# KeyError 2 - no parent
# c.add_category('D', 'E')

# KeyError 3 - unique name
# c.add_category('D', 'C')
c.add_category('D', 'B')

# Simple case
c.add_category('G', 'B')
c.add_category('H', 'B')


print(','.join(c.get_children('A') or []))
print(','.join(c.get_children('B') or []))

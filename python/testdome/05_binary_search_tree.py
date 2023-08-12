"""
5. Binary Search Tree

Binary search tree (BST) is a binary tree where the value of each node
is larger or equal to the values in all the nodes in that node's left
subtree and is smaller than the values in all the nodes in that node's
right subtree.

Write a function that, efficiently with respect to time used,
checks if a given binary search tree contains a given value.

For example, for the following tree:

n1 (Value: 1, Left: null, Right: null)
n2 (Value: 2, Left: n1, Right: n3)
n3 (Value: 3, Left: null, Right: null)
Call to contains(n2, 3) should return True since a tree with root
at n2 contains number 3.


Time : 16.30 (min)
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Correctness: Correct answer
  Performance test on a large tree: Correct answer


* Subject - binary tree

* Learning
    1. The way of return returned response in a recursive function (True)

"""


import collections


class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):
        # 1) while loop
        # node = root
        #
        # while node:
        #     if node.value == value:
        #         return True
        #     elif node.value < value:
        #         node = node.right
        #     else:
        #         node = node.left
        # return False

        # 2) recursion
        # if not root:
        #     return False
        #
        # if root.value == value:
        #     return True
        # elif root.value < value:
        #     root = root.right
        # else:
        #     root = root.left
        #
        # result = BinarySearchTree.contains(root, value)
        # if result:
        #     return True

        # 3) recursion refactored
        if not root:
            return False
        if root.value < value:
            return BinarySearchTree.contains(root.right, value)
        elif root.value > value:
            return BinarySearchTree.contains(root.left, value)
        else:
            return True


n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 3))


"""
181111 Review

Time : 16.30 (min)
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Correctness: Correct answer
  Performance test on a large tree: Correct answer
"""

"""
181129 Review 2

Time : 10 (min)
Tests: 3 pass / 0 fail
  Example case: Correct answer
  Correctness: Correct answer
  Performance test on a large tree: Correct answer
"""

import collections


class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):
        # 1) while loop (without recursion)
        # node = root
        # while node:
        #     if node.value == value:
        #         return True
        #     if node.value > value:
        #         node = node.left
        #     elif node.value < value:
        #         node = node.right
        # return False

        # 2) recursion
        node = root
        if node is None:
            return False

        if node.value == value:
            return True
        if node.value > value:
            return BinarySearchTree.contains(node.left, value)
        if node.value < value:
            return BinarySearchTree.contains(node.right, value)


n1 = BinarySearchTree.Node(value=1, left=None, right=None)
n3 = BinarySearchTree.Node(value=3, left=None, right=None)
n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

print(BinarySearchTree.contains(n2, 1))


"""
230807 Review 4

Time: 20 (min)
Code:
"""

## Needs to be refactored as the above two solutions ##

# class BinarySearchTree:
#     Node = collections.namedtuple('Node', ['left', 'right', 'value'])

#     @staticmethod
#     def contains(root, value):
#         # print(root)
#         # print(root.left)
#         # print(root.right)
#         # print(root.value)

#         if root.value == value:
#             return True
#         elif root.value > value:
#             print(11)
#             if root.left:
#                 return BinarySearchTree.contains(root.left, value)
#             else:
#                 return False
#         elif root.value < value:
#             print(22)
#             if root.right:
#                 return BinarySearchTree.contains(root.right, value)
#             else:
#                 return False
#         else:
#             return False

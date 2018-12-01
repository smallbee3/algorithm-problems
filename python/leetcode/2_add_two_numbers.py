"""
2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers.
 The digits are stored in reverse order and each of their nodes contain a single digit.
  Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

"""
Time : (more than) 60 min

* Subject - Linked List
* Learning
    1. Should start from the 'last node' when making linked list in python
    2. The place of 'break' when make a for loop for linked list
        181201
        -> Just using 'while node:' instead
    
    3. Power of pseudo code, simple
    
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # l1_num = 0
        # l2_num = 0
        #
        # for idx, i in enumerate(l1):
        #     # if idx == 0:
        #     #     l1_num += i
        #     # else:
        #     #     l1_num = l1_num + i * 10 ** idx
        #     l1_num = l1_num + i * 10 ** idx if not idx == 0 else l1_num + i
        #
        # for idx, i in enumerate(l2):
        #     l2_num = l2_num + i * 10 ** idx if not idx == 0 else l2_num + i
        #
        # sum = l1_num + l2_num
        #
        # sum_list = []
        # for i in str(sum):
        #     sum_list.insert(0, i)
        #
        # return sum_list

        def print_node(l):
            while True:
                print(l.val, end=' -> ') if l.next else print(l.val)
                if l.next is None:
                    break
                l = l.next

        l1_num = 0
        l2_num = 0

        i = 0
        while True:
            l1_num = l1_num + l1.val * 10 ** i if not i == 0 else l1_num + l1.val
            i += 1
            if not l1.next:
                break
            l1 = l1.next

        i = 0
        while True:
            l2_num = l2_num + l2.val * 10 ** i if not i == 0 else l2_num + l2.val
            i += 1
            if not l2.next:
                break
            l2 = l2.next

        sum = l1_num + l2_num
        sum_str = str(sum)

        node = ListNode(sum_str[0])
        for idx, i in enumerate(sum_str[1:]):
            next_node = ListNode(int(i))
            next_node.next = node
            node = next_node

        print_node(node)
        return node

        # * Fail - cannot find root node after the process

        # reverse_sum = []
        # for i in str(sum):
        #     reverse_sum.insert(0, int(i))
        #
        # l3 = ListNode(reverse_sum[0])
        #
        # for i in reverse_sum[1:]:
        #     node = ListNode(i)
        #     l3.next = node
        #     l3 = l3.next


if __name__ == '__main__':

    l1 = ListNode(2)
    l2 = ListNode(4)
    l3 = ListNode(3)
    l1.next = l2
    l2.next = l3

    l4 = ListNode(5)
    l5 = ListNode(6)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6

    solution = Solution()
    solution.addTwoNumbers(l1, l4)


"""

181201 Review

Time : 13 min

The code below is simpler than the above in two ways.
First, the one above make a non reverse number by multiplying 10**i.
       it is not easy to think instantly.
Second, no need to make a last node outside of loop like 'node = ListNode(sum_str[0])'
      There is better way as the code below using 'prev_node=None'

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def make_num(node):
            str_num = ''
            while node:
                str_num = str(node.val) + str_num
                node = node.next

            return int(str_num)

        num1 = make_num(l1)
        num2 = make_num(l2)

        num3_str = str(num1 + num2)

        node = None
        prev_node = None
        for i in num3_str:
            node = ListNode(int(i))

            if prev_node:
                node.next = prev_node
            prev_node = node

        return node


def make_node(num):

    str_num = str(num)

    node = None
    prev_node = None
    for i in str_num:
        node = ListNode(int(i))

        if prev_node:
            node.next = prev_node
        prev_node = node

    return node


num1 = 342
num2 = 465
l1 = make_node(num1)
l2 = make_node(num2)


solution = Solution()
l3 = solution.addTwoNumbers(l1, l2)

node = l3
while node:
    print(node.val, end=' -> ' if node.next is not None else '')
    node = node.next

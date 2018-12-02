"""
21. Merge Two Sorted Lists


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

"""

"""
181118

(1) Runtime Error
Line 45: AttributeError: 'NoneType' object has no attribute 'val'

>> while True 
    -> while node:


(2) Wrong Answer
Output: [(5, 1),(4, 1),(3, 2),(2, 3),(1, 4),(0, 4)]
Expected: [1,1,2,3,4,4]

>> for i in <list> 
    -> for idx, i in enumerate(<list>):

"""

# Definition for singly-linked list.
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def quick_sort(arr):

            if len(arr) < 2:
                return arr
            else:
                pivot = random.randrange(len(arr))
                a = []
                b = []
                for i in range(len(arr)):
                    if arr[i] > arr[pivot]:
                        a.append(arr[i])
                    elif i == pivot:
                        pass
                    else:
                        b.append(arr[i])

                return quick_sort(a) + [arr[pivot]] + quick_sort(b)

        def print_node(l):
            while l:
                print(l.val, end='->') if l.next else print(l.val)
                l = l.next

        def node_to_list(node):
            node_list = []

            # 181202 The mistake found
            # 'while True' allow None type value pass through
            # so, None type value made an error at 'node.val'

            # while True:
            #     node_list.append(node.val)
            #     if node.next is None:
            #         return node_list
            #     node = node.next
            while node:
                node_list.append(node.val)
                node = node.next
            return node_list

        l1_list = node_to_list(l1)
        l2_list = node_to_list(l2)
        l3_list = quick_sort(l1_list + l2_list)

        node = None

        # 181202 The mistake found (2)
        # for i in enumerate(l3_list):
        #     if i == 0:
        #         node = ListNode(i)
        #         continue
        #     prev_node = ListNode(i)
        #     prev_node.next = node
        #     node = prev_node

        for idx, i in enumerate(l3_list):
            if idx == 0:
                node = ListNode(i)
                continue
            prev_node = ListNode(i)
            prev_node.next = node
            node = prev_node

        l3 = node
        print_node(l3)
        return l3


if __name__ == '__main__':

    l1 = ListNode(1)
    l1_2 = ListNode(2)
    l1_3 = ListNode(4)
    l1.next = l1_2
    l1_2.next = l1_3

    l2 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)
    l2.next = l2_2
    l2_2.next = l2_3

    solution = Solution()
    solution.mergeTwoLists(l1, l2)


"""

181201 Review

Time : 13 min

"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []

        node = l1
        while node:
            list1.append(node.val)
            node = node.next

        node = l2
        while node:
            list2.append(node.val)
            node = node.next

        list3 = sorted(list1 + list2)

        node = None
        pre_node = None
        for i in list3[::-1]:
            node = ListNode(i)
            if pre_node:
                node.next = pre_node
            pre_node = node

        return node


if __name__ == '__main__':

    def print_linked_list(node):
        while node:
            print(node.val, end='->' if node.next is not None else '')
            node = node.next

    def make_linked_list(num):

        str_num = str(num)

        node = None
        pre_node = None
        for i in str_num[::-1]:
            node = ListNode(int(i))
            if pre_node:

                # This one mistake costs 30 minutes !
                # node = node.next
                node.next = pre_node
            pre_node = node

        return node


    input1 = 124
    input2 = 134
    l1 = make_linked_list(input1)
    l2 = make_linked_list(input2)

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    print_linked_list(result)

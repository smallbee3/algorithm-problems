"""
21. Merge Two Sorted Lists


Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

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
            while True:
                print(l.val, end=' -> ') if l.next else print(l.val)
                if l.next is None:
                    break
                l = l.next

        # print_node(l1)
        # print_node(l2)

        def node_to_list(l):
            node_list = []
            while True:
                node_list.append(l.val)
                if l.next is None:
                    return node_list
                l = l.next

        l1_list = node_to_list(l1)
        l2_list = node_to_list(l2)

        l3_list = l1_list + l2_list
        l3_list = quick_sort(l3_list)
        # print(l3_list)

        node = None
        for i in l3_list:
            if i == 0:
                node = ListNode(i)
                continue
            prev_node = ListNode(i)
            prev_node.next = node
            node = prev_node

        l3 = node
        # print_node(l3)
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
    print(solution.mergeTwoLists(l1, l2))

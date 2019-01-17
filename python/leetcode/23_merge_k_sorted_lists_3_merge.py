"""
181213 (3)

Time : 9 min

Runtime: 80 ms,
faster than 86.74% of Python3 online submissions for Merge k Sorted List

Subject -

Learning
    1. Setting max value
        0       (x)
        -1      (x)
        arr[0]  (x)  (this may take time of O(N) because some element is none, e.g. [[2->3->5], [], [-2->4]] )
        -float('inf') (o)

    2. ListNode exception handling of [[]], [[], []], ...

    3. Integrate separated lists into one list when it is possible
        -> Solving the time limit exceed problem

    4. The technique of remove element in the list
        check from the front    (x)
        check from the last     (o)
        make a element list to remove (o)

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @classmethod
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def find_the_max_node(lists_list):

            max = lists_list.pop()
            return max

        node = None
        prev_node = None

        # '[]' exception handling

        # 1) check from the front
        # for idx, i in enumerate(lists):
        #     if not isinstance(i, ListNode):
        #         del lists[idx]

        # 2) check from the last
        length = len(lists)
        for i in range(length):
            idx = length - 1 - i
            if not isinstance(lists[idx], ListNode):
                del lists[idx]

        # 3) make a element list to remove
        # remove_list = []
        # for idx, i in enumerate(lists):
        #     if not isinstance(i, ListNode):
        #         remove_list.insert(0, idx)
        # for i in remove_list:
        #     del lists[i]

        # 2) < 3) because ... ?

        # 23_merge_k_sorted_lists_3_merge
        # Merge every linked list
        lists_list = []
        if lists:
            for idx, node in enumerate(lists):
                while node:
                    lists_list.append(node.val)
                    node = node.next
            lists_list.sort()

        while lists_list:
            max = find_the_max_node(lists_list)
            node = ListNode(max)

            if prev_node:
                node.next = prev_node
            prev_node = node

        return node


if __name__ == '__main__':

    def make_node(alist):

        node = None
        prev_node = None
        while alist:

            node = ListNode(alist.pop())

            if prev_node:
                node.next = prev_node
            prev_node = node
        return node


    def print_node(node):

        while node:
            print(node.val, end='->' if node.next is not None else '\n')
            node = node.next


    node_list = []
    node = make_node([1, 4, 5])
    print_node(node)
    node_list.append(node)

    node = make_node([1, 3, 4])
    print_node(node)
    node_list.append(node)

    node = make_node([2, 6])
    print_node(node)
    node_list.append(node)

    node_list.append([])

    # result = Solution.mergeKLists(node_list)

    # 1) exception handling for [[]]
    # result = Solution.mergeKLists([[]])

    # 2) exception handling for [[], []]
    # result = Solution.mergeKLists([[], []])

    # 3) exception handling for [[2],[],[-1]]
    node_list = []
    node = make_node([2])
    print_node(node)
    node_list.append(node)

    node_list.append([])

    node = make_node([-1])
    print_node(node)
    node_list.append(node)

    result = Solution.mergeKLists(node_list)

    print_node(result)

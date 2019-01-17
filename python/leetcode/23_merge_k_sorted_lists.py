"""
23_merge_k_sorted_lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.


Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def mergeKLists(self, lists):
#         :type lists: List[ListNode]
#         :rtype: ListNode
        

"""

"""
181213

Time : 73 min

    130 / 131 test cases passed.
    Time Limit Exceeded
    Last executed input:
    [[7],[49],[73],[58],[30],[72],[44],[78],[23],[9],[40],[65],[92],[42],[87],[3], ....


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

        def find_the_max_node(lists):
            # 181213
            # max = 0 # -> [[0,2,5]] : TypeError: list indices must be integers or slices, not NoneType
            # max = -1 # -> [[2],[],[-1]] : TypeError: list indices must be integers or slices, not NoneType
            max = -float('inf')
            max_idx = None
            for idx, node in enumerate(lists):

                while node.next:
                    node = node.next

                if max < node.val:
                    max = node.val
                    max_idx = idx

            node = lists[max_idx]
            while True:
                # 1 delete the last(maximum) node
                if node.next is None:
                    # 181213 infinite loop problem
                    # del node

                    del lists[max_idx]
                    break

                # 2 change 'next' link of a previous node None into 'None'
                if node.next.next is None:
                    node.next = None
                    break
                node = node.next
            return max

        # '[]' exception handling

        # 1) check from the front
        # for idx, i in enumerate(lists):
        #     if not isinstance(i, ListNode):
        #         del lists[idx]

        # 2) check from the last
        # for i in range(len(lists)):
        #     idx = len(lists) - 1 - i
        #     if not isinstance(lists[idx], ListNode):
        #         del lists[idx]

        # 3) make a element list to remove
        remove_list = []
        for idx, i in enumerate(lists):
            if not isinstance(i, ListNode):
                # insert to the first -> remove from the last index in the remove_list
                remove_list.insert(0, idx)
        for i in remove_list:
            del lists[i]

        node = None
        prev_node = None
        while lists:
            max = find_the_max_node(lists)
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


    # node_list = []
    # node = make_node([1, 4, 5])
    # print_node(node)
    # node_list.append(node)
    #
    # node = make_node([1, 3, 4])
    # print_node(node)
    # node_list.append(node)
    #
    # node = make_node([2, 6])
    # print_node(node)
    # node_list.append(node)
    #
    # node_list.append([])

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

    print(node_list)

    result = Solution.mergeKLists(node_list)

    print_node(result)

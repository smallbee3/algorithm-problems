"""
181213 (2)

Time : 40 min

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

        def find_the_max_node(lists_dict):
            max = -float('inf')
            max_idx = None

            for i in lists_dict:
                alist = lists_dict[i]
                if max < alist[len(alist) - 1]:
                    max = alist[len(alist) - 1]
                    max_idx = i

            lists_dict[max_idx].pop()
            if lists_dict[max_idx] == []:
                del lists_dict[max_idx]

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
                remove_list.insert(0, idx)
        for i in remove_list:
            del lists[i]

        # Time efficiency issue

        # 23_merge_k_sorted_lists_2_dict
        # Use dictionary
        lists_dict = {}
        if lists:
            for idx, node in enumerate(lists):
                while node:
                    if lists_dict.get(idx):
                        lists_dict[idx].append(node.val)
                    else:
                        lists_dict[idx] = [node.val]
                    node = node.next
            print(lists_dict)

        node = None
        prev_node = None

        # while lists:
        while lists_dict:
            max = find_the_max_node(lists_dict)
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

    result = Solution.mergeKLists(node_list)

    # 1) exception handling for [[]]
    # result = Solution.mergeKLists([[]])

    # 2) exception handling for [[], []]
    # result = Solution.mergeKLists([[], []])

    # 3) exception handling for [[2],[],[-1]]
    # node_list = []
    # node = make_node([2])
    # print_node(node)
    # node_list.append(node)
    #
    # node_list.append([])
    #
    # node = make_node([-1])
    # print_node(node)
    # node_list.append(node)
    #
    # result = Solution.mergeKLists(node_list)

    print_node(result)

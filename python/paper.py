# 01
# 5.37 min
def group_by_owners(dict):
    """
    {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    """
    adict = {}
    for key, value in dict.items():
        if adict.get(value):
            # if key in adict[value]:
            #     continue
            # else:
            adict[value].append(key)
        else:
            adict[value] = [key]
    return adict


# if __name__ == "__main__":
#     files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy', 'Output.txt': 'Randy'}
#     print(group_by_owners(files))


# 02
class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if len(self.ingredients) == 0 or len(self.toppings) == 0:
            return []

        comb_list = []
        for i in self.ingredients:
            for t in self.toppings:
                comb_list.append([i, t])
        return comb_list


# if __name__ == "__main__":
#     print(IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops())
#     print(IceCreamMachine(["i1", ], ["t1", "t2", "t3"]).scoops())

#     m = 2
#     n = 3
#     matrix = [[(i, j) for i in range(m)] for j in range(n)]
#     print(matrix)

#     matrix = [(i, j) for i in range(m) for j in range(n)]
#     print(matrix)


# 03
class MergeNames:
    @staticmethod
    def unique_names(names1, names2):
        aset = set(names1)
        aset.update(names2)
        return list(aset)

    @staticmethod
    def unique_names2(names1, names2):
        for i in names2:
            if not i in names1:
                names1.append(i)
        return list(set(names1))


# if __name__ == "__main__":
#     print(MergeNames.unique_names(["Ava", "Emma", "Olivia", "Emma"], ["Olivia", "Sophia", "Emma"]))
#     print(MergeNames.unique_names2(["Ava", "Emma", "Olivia", "Emma"], ["Olivia", "Sophia", "Emma"]))

#     (O)
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(names1 + names1)

#     names1 = set(["Ava", "Emma", "Olivia"])
#     names2 = set(["Olivia", "Sophia", "Emma"])

#     # print(names1 + names2) # (X)
#     print(names1 - names2)
#     print(names1 | names2)
#     print(names1 & names2)


# 04
class Palindrome:
    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        num_of_word = len(word)

        if num_of_word == 0:
            return False

        if num_of_word % 2 == 0:
            for i in range(num_of_word // 2):
                if word[i] != word[num_of_word - i - 1]:
                    return False

        else:
            for i in range(num_of_word // 2):
                if word[i] != word[num_of_word - i - 1]:
                    return False

        return True


# if __name__ == "__main__":
#     print(Palindrome.is_palindrome('Deleveled'))
#     print(Palindrome.is_palindrome('delled'))


# 05
import collections


class BinarySearchTree:
    Node = collections.namedtuple('Node', ['left', 'right', 'value'])

    @staticmethod
    def contains(root, value):
        # print(root)
        # print(root.left)
        # print(root.right)
        # print(root.value)

        # if root.value == value:
        #     return True
        # elif root.value > value:
        #     # print(11)
        #     if root.left:
        #         return BinarySearchTree.contains(root.left, value)
        #     else:
        #         return False
        # elif root.value < value:
        #     # print(22)
        #     if root.right:
        #         return BinarySearchTree.contains(root.right, value)
        #     else:
        #         return False
        # else:
        #     return False

        node = root
        while node:
            if node.value == value:
                return True
            if node.value > value:
                node = node.left
            elif node.value < value:
                node = node.right
        return False


# if __name__ == "__main__":
#     n1 = BinarySearchTree.Node(value=1, left=None, right=None)
#     n3 = BinarySearchTree.Node(value=3, left=None, right=None)
#     n2 = BinarySearchTree.Node(value=2, left=n1, right=n3)

#     print(BinarySearchTree.contains(n2, 3))


# 25min
# 06
# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

#     def next_song(self, song):
#         self.next = song

#     def is_repeating_playlist(self):
#         """
#         :returns: (bool) True if the playlist is repeating, False if not.
#         """
#         if not self or self.next is None:
#             return False

#         first_song_name = self.name
#         curr_song = self

#         while curr_song:
#             if curr_song.next.next and curr_song.next.next.name == first_song_name:
#                 return True
#             curr_song = curr_song.next

#         return False


class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        if not self or self.next is None:
            return False

        curr_song = self
        song_name_list = []

        while curr_song:
            song_name_list.append(curr_song.name)
            if curr_song.next and curr_song.next.name in song_name_list:
                return True
            curr_song = curr_song.next

        return False


# if __name__ == "__main__":
#     first = Song("Hello")
#     second = Song("Eye of the tiger")

#     first.next_song(second)
#     second.next_song(first)

#     print(first.is_repeating_playlist())

#     first = Song("A")
#     second = Song("B")
#     third = Song("C")
#     fourth = Song("D")

#     first.next_song(second)
#     second.next_song(third)
#     third.next_song(fourth)
#     # fourth.next_song(None)
#     fourth.next_song(first)

#     print(first.is_repeating_playlist())


# 07
class TwoSum:
    @staticmethod
    def find_two_sum(numbers, target_sum):
        # 1) two ranges
        # 14.13 min
        # for i in range(len(numbers) - 1):
        #     for j in range(len(numbers) - i - 1):
        #         j = j + i + 1
        #         # print('i, j: ', i, j)
        #         sub_target = target_sum - numbers[i]
        #         if numbers[j] == sub_target:
        #             return i, j
        # return None

        # 2)
        # 11.04 min
        adict = {}
        for idx, i in enumerate(numbers):
            if adict.get(i):
                adict[i].append(idx)
            else:
                adict[i] = [idx]

        for k, v in adict.items():
            sub_target = target_sum - k

            if adict.get(sub_target):
                idxes = adict[sub_target]
                if sub_target == k and len(idxes) > 1:
                    return idxes[0], idxes[1]
                if sub_target != k:
                    return v[0], idxes[0]
        return None


# if __name__ == "__main__":
#     print(TwoSum.find_two_sum([3, 3, 5, 7, 5, 9], 10))
#     print(TwoSum.find_two_sum([5, 1, 2, 7, 3, 9], 10))
#     print(TwoSum.find_two_sum([1, 1, 5, 7, 5, 8], 10))


# 09

from collections import Counter
from collections import OrderedDict


class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])

    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score

    def compare_player(self, i, j):
        pass


# if __name__ == "__main__":
#     table = LeagueTable(['Mike', 'Chris', 'Arnold'])
#     table.record_result('Mike', 2)
#     table.record_result('Mike', 3)
#     table.record_result('Arnold', 5)
#     table.record_result('Chris', 5)
#     print(table.player_rank(1))

# table = LeagueTable(['Mike', 'Chris', 'Arnold'])
# table.record_result('Mike', 2)
# table.record_result('Mike', 3)
# table.record_result('Arnold', 5)
# table.record_result('Chris', 1)
# print(table.player_rank(1))


# 12
class CategoryTree:
    def __init__(self):
        self.category_dict = {}

    def add_category(self, category, parent):
        if category in self.category_dict:
            raise Exception('category already exist')

        if parent is None:
            self.category_dict[category] = []
        else:
            self.category_dict[category] = []
            self.category_dict[parent].append(category)

    def get_children(self, parent):
        return self.category_dict[parent]


if __name__ == "__main__":

    # 1) Basic test case
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))
    print(','.join(c.get_children('B') or []))
    print(','.join(c.get_children('C') or []))

    # 2) Complex test case
    c.add_category('D', 'B')
    c.add_category('E', 'B')
    c.add_category('F', 'C')
    c.add_category('G', 'C')
    c.add_category('H', 'C')
    print(','.join(c.get_children('A') or []))
    print(','.join(c.get_children('B') or []))
    print(','.join(c.get_children('C') or []))

    # 3) KeyError test case
    # c.add_category('I', 'Z')

    # 4) Exception test case
    # c.add_category('H', 'C')

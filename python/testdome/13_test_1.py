"""
181113

Time : 13 min

"""

class Rare:

    @staticmethod
    def nth_most_rare(elements, n):

        rare_dict = {}
        for i in elements:
            if rare_dict.get(i):
                rare_dict[i] += 1
                continue
            rare_dict[i] = 1

        rank_list = [list(rare_dict.keys())[0]]

        for i in list(rare_dict.keys())[1:]:
            for idx, j in enumerate(rank_list):
                if rare_dict[i] < rare_dict[j]:
                    rank_list.insert(idx, i)
                    break
                if idx == len(rank_list) - 1:
                    rank_list.insert(idx+1, i)
                    break

        return rank_list[n-1]


print(Rare.nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))


"""
181202 Review

Time : 14 min

Learning:
    1. Need break when inserting the node in the last loop into new sorted_list

"""


class Rare:

    @staticmethod
    def nth_most_rare(elements, n):

        adict = {}
        for i in elements:
            if adict.get(i):
                adict[i] += 1
            else:
                adict[i] = 1

        # sorted_adtic = sorted(adict, key=adict.values)

        sorted_list = [list(adict.keys())[0]]

        for i in list(adict.keys())[1:]:
            for idx, j in enumerate(sorted_list):
                if adict[i] < adict[j]:
                    sorted_list.insert(idx, i)
                    break
                if idx == len(sorted_list)-1:
                    sorted_list.insert(idx+1, i)
                    break

        return sorted_list[n-1]


print(Rare.nth_most_rare([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))

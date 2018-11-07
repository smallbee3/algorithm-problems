
# 03 Merge Names

# Implement the unique_names method. When passed two arrays of names,
# it will return an array containing the names that appear in either or both arrays.
# The returned array should have no duplicates.

# For example, calling MergeNames.unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
# should return an array containing Ava, Emma, Olivia, and Sophia in any order.


# (Time: 10.14 minutes)
# Tests: 4 pass / 0 fail
#   Example case: Correct answer
#   Each array has distinct names: Correct answer
#   Each array has duplicate names: Correct answer
#   Arrays have some names in common: Correct answer


class MergeNames:

    # 1) Using 'set'
    # @staticmethod
    # def unique_names(names1, names2):
    #     names1.extend(names2)
    #     return list(set(names1))

    # 2) Using 'set' + for loop
    # @staticmethod
    # def unique_names(names1, names2):
    #
    #     for i in names2:
    #         if not i in names1:
    #             names1.append(i)
    #     return list(set(names1))

    # 3) Not using set at all
    @staticmethod
    def unique_names(names1, names2):

        for i in names2:
            if not i in names1:
                names1.append(i)

        result_list = []
        for j in names1:
            if not j in result_list:
                result_list.append(j)

        return result_list


names1 = ["Ava", "Emma", "Olivia", "Emma"]
names2 = ["Olivia", "Sophia", "Emma"]
print(MergeNames.unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia

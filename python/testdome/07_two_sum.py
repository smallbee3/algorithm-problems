"""
7. Two Sum

Write a function that, when passed a list and a target sum, returns, efficiently with respect to
time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to
the target sum. If there are no two numbers, the function should return None.

For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the
following pairs of indices:

0 and 3 (or 3 and 0) as 3 + 7 = 10
1 and 5 (or 5 and 1) as 1 + 9 = 10
2 and 4 (or 4 and 2) as 5 + 5 = 10


* Subject - Eradicate duplicate elements

* Learning
    1. When put list's index, element into dictionary,
       Key : element , Value : [index]
       (Because if put element into Value, No way to find the value.
        So, put element into Value, but input indexes as a list for duplicate issue.)

    2. Do not use "list.index(x)", "x in [list]" etc on a problem with time efficiency issue

    3. 'key in dict' is as fast as 'dict.get(key)', I guess
"""


class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        Time : (more than) 40 min
        Tests: 3 pass / 1 fail
          Example case: Correct answer
          Distinct numbers with and without solutions: Correct answer
          Duplicate numbers with and without solutions: Correct answer
          Performance test with a large list of numbers: Time limit exceeded
        """
        """
        # 1) 1 for loop + 'in' + 'index' - O(n³)
        """
        # for i_num, i in enumerate(numbers):
        #     j = target_sum - i
        #     temp_list = numbers.copy()
        #     temp_list.pop(i_num)
        #     print(temp_list)
        #     if j in temp_list:
        #         j_num = numbers.index(j)
        #         if j_num != i_num:
        #             return i_num, j_num
        #         else:
        #             # 1) for loop
        #             # for k_num, k in enumerate(numbers):
        #             #     if k == j and i_num != k_num:
        #             #         return i_num, k_num
        #             # 2) change the first same element
        #             numbers[j_num] = -1
        #             return i_num, numbers.index(j)
        # return None
        """
        2) two for loop - O(n²)
        """
        # for i in range(len(numbers)):
        #
        #     for j in range(len(numbers)):
        #         if j == i:
        #             continue
        #         if numbers[i] + numbers[j] == target_sum:
        #             return i, j
        """
        3) dict + "num in dict1"

        Time : 52 min
        Tests: 4 pass / 0 fail
          Example case: Correct answer
          Distinct numbers with and without solutions: Correct answer
          Duplicate numbers with and without solutions: Correct answer
          Performance test with a large list of numbers: Correct answer
        """
        dict1 = {}
        for i_num, i in enumerate(numbers):

            # To cope with 'numbers' having duplicate numbers
            if dict1.get(i):
                dict1[i] += [i_num]
            else:
                dict1[i] = [i_num]

        for key, value in dict1.items():
            target_num = target_sum - key
            if target_num in dict1:

                if key != target_num:
                    return dict1[key][0], dict1[target_num][0]

                elif key == target_num and len(dict1[key]) > 1:
                    return dict1[key][0], dict1[key][1]


print(TwoSum.find_two_sum([3, 3, 5, 7, 5, 9], 10))


"""
181111 Review

Time : 17 (min)
Tests: 4 pass / 0 fail
  Example case: Correct answer 
  Distinct numbers with and without solutions: Correct answer 
  Duplicate numbers with and without solutions: Correct answer 
  Performance test with a large list of numbers: Correct answer 
"""


class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """

        number_dict = {}
        for idx, i in enumerate(numbers):
            if number_dict.get(i):
                number_dict[i] += [idx]
            else:
                number_dict[i] = [idx]

        for key in number_dict.keys():
            num = target_sum - key
            # if num in number_dict:
            if number_dict.get(num):

                # 1) fail - because the exception case go to else: directly
                # if num == key and len(number_dict[num]) > 1:
                #     print(number_dict[key][0], number_dict[num][1])
                #     return number_dict[key][0], number_dict[num][1]
                # else:
                #     print(number_dict[key][0], number_dict[num][0])
                #     return number_dict[key][0], number_dict[num][0]

                # 2) pass
                # if num == key:
                #     if len(number_dict[num]) > 1:
                #         print(number_dict[key][0], number_dict[num][1])
                #         return number_dict[key][0], number_dict[num][1]
                # else:
                #     print(number_dict[key][0], number_dict[num][0])
                #     return number_dict[key][0], number_dict[num][0]

                # 3) pass (But I didn't know there could be a flaw)
                if num != key:
                    print(number_dict[key][0], number_dict[num][0])
                    return number_dict[key][0], number_dict[num][0]
                elif num == key and len(number_dict[num]) > 1:
                    print(number_dict[key][0], number_dict[num][1])
                    return number_dict[key][0], number_dict[num][1]
        return None


print(TwoSum.find_two_sum([5, 1, 2, 7, 3, 9], 10))


"""
181129 Review 2

Time : 14 (min)
Tests: 3 pass / 1 fail
  Example case: Correct answer 
  Distinct numbers with and without solutions: Correct answer 
  Duplicate numbers with and without solutions: Correct answer 
  * Performance test with a large list of numbers: Time limit exceeded
"""


# class TwoSum:
#
#     @staticmethod
#     def find_two_sum(numbers, target_sum):
#         """
#         :param numbers: (list of ints) The list of numbers.
#         :param target_sum: (int) The required target sum.
#         :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
#         """
#
#         for i in range(len(numbers)):
#             numbers2 = numbers.copy()
#             num = target_sum - numbers[i]
#             if num in numbers:
#                 if num != numbers[i]:
#                     return i, numbers.index(num)
#                 else:
#                     del numbers2[i]
#                     if num in numbers2:
#                         return i, numbers2.index(num)+1
#         return None


"""
181129 Review 2

Time : 10 (min)
Tests: 4 pass / 0 fail
  Example case: Correct answer 
  Distinct numbers with and without solutions: Correct answer 
  Duplicate numbers with and without solutions: Correct answer 
  Performance test with a large list of numbers: Correct answer 
"""


class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """

        dict1 = {}
        for idx, i in enumerate(numbers):
            if dict1.get(i):
                dict1[i].append(idx)
            else:
                dict1[i] = [idx]

        for i in numbers:
            num = target_sum - i

            # (x) 'in' made a loop
            # if num in numbers:

            # 181129
            # 1) This also works !
            if num in dict1:

            # 2)
            # if dict1.get(num):

                if i != num:
                    return dict1[i][0], dict1[num][0]
                if len(dict1[i]) > 1:
                    return dict1[i][0], dict1[i][1]
        return None


print(TwoSum.find_two_sum([1, 1, 5, 7, 5, 8], 10))


# 07 Two Sum

# Write a function that, when passed a list and a target sum, returns, efficiently with respect to
# time used, two distinct zero-based indices of any two of the numbers, whose sum is equal to
# the target sum. If there are no two numbers, the function should return None.

# For example, find_two_sum([3, 1, 5, 7, 5, 9], 10) should return a single tuple containing any of the
# following pairs of indices:

# 0 and 3 (or 3 and 0) as 3 + 7 = 10
# 1 and 5 (or 5 and 1) as 1 + 9 = 10
# 2 and 4 (or 4 and 2) as 5 + 5 = 10


class TwoSum:

    @staticmethod
    def find_two_sum(numbers, target_sum):
        """
        :param numbers: (list of ints) The list of numbers.
        :param target_sum: (int) The required target sum.
        :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
        """
        """
        1) Fail : Time limit exceeded

        Time : (more than) 40 min
        Tests: 3 pass / 1 fail
          Example case: Correct answer 
          Distinct numbers with and without solutions: Correct answer 
          Duplicate numbers with and without solutions: Correct answer 
          Performance test with a large list of numbers: Time limit exceeded 
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
        2) two for loop
        """
        # for i in range(len(numbers)):
        #
        #     for j in range(len(numbers)):
        #         if j == i:
        #             continue
        #         if numbers[i] + numbers[j] == target_sum:
        #             return i, j

        """
        3) dict

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

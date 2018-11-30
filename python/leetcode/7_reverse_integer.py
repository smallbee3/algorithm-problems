"""
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

"""
Time : 30 min

* Subject - reverse 32-bit digit
* Learning
    1. 32 bit number
    2. minus integer <-> string
    3. handling minus number
    4. number range point (when number is reversed)

    181130
    5. make a reversed number with str
        e.g. num_str_reverse = i + num_str_reverse

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # 181130
        # missed point (e.g. x = 2200000000)
        # 32-bit signed integer validation
        if not -2**31 <= x < 2**31-1:
            return 0

        minus = 0
        if not x >= 0:
            num_str = str(x)[1:]
            minus += 1
        else:
            num_str = str(x)

        num_str_reverse = ''
        for i in num_str:
            num_str_reverse = i + num_str_reverse

        if minus:
            result = int('-' + num_str_reverse)
        else:
            result = int(num_str_reverse)

        # 32-bit signed integer validation
        if result > 2**31-1 or result < -2**31:
            return 0

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(1534236469))
    print(solution.reverse(2147483648))
    print(solution.reverse(2200000000))  # -> exception case

    # print(int('000123'))
    # print(int('-000123'))
    # print(2**31-1)
    # print(-2**31)


"""
181130 Review 2

Time : 20 min

"""

# 181130
# I like the code above which makes reversed number with str
# The way using list indexing below is slower


# class Solution:
#
#     @classmethod
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#
#         # 32-bit signed integer validation
#         if not -2**31 <= x < 2**31-1:
#             return 0
#
#         str_num = str(x)
#         is_num_minus = False
#
#         if str_num.startswith('-'):
#             str_num = str_num[1:]
#             is_num_minus = True
#
#         list_num = list(str_num)
#
#         for i in range(len(list_num) // 2):
#             list_num[i], list_num[len(list_num)-i-1] = list_num[len(list_num)-i-1], list_num[i]
#
#         str_num = ''.join(list_num)
#         if is_num_minus is True:
#             str_num = '-' + str_num
#
#         # 32-bit signed integer validation
#         if not -2**31 <= int(str_num) < 2**31-1:
#             return 0
#
#         return int(str_num)
#
#
# print()
# # print(Solution.reverse(12))
# print(Solution.reverse(2200000000))
#
# # 2**31 -1 = 2147483647

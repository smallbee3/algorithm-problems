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

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = 0
        if not x >= 0:
            reverse_num = str(x)[1:]
            minus += 1
        else:
            reverse_num = str(x)

        reverse_num_str = ''
        for i in reverse_num:
            reverse_num_str = i + reverse_num_str

        if minus:
            result = int('-' + reverse_num_str)
        else:
            result = int(reverse_num_str)

        if result > 2**31-1 or result < -2**31:
            return 0

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(1534236469))
    print(solution.reverse(2147483648))

    # print(int('000123'))
    # print(int('-000123'))
    # print(2**31-1)
    # print(-2**31)

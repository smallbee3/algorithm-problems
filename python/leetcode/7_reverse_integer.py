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
        e.g.
        int('001') -> 1
        int('-021') -> -21
    3. handling minus number
    4. number range changes when number is reversed

    181130
    5. make a reversed number with str
        e.g. num_str_reverse = ''; num_str_reverse = i + num_str_reverse

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
        if not -2**31 <= x <= 2**31-1:
            return 0

        minus = False
        if not x >= 0:
            num_str = str(x)[1:]
            minus = True
        else:
            num_str = str(x)

        # 1) reverse using 'string' (84 ms)
        # num_str_reverse = ''
        # for i in num_str:
        #     num_str_reverse = i + num_str_reverse

        # 2) reverse using 'list' and 'tuple unpacking' (84 ms)
        num_reverse = list(num_str)
        for i in range(len(num_reverse) // 2):
            num_reverse[i], num_reverse[len(num_reverse)-i-1] = num_reverse[len(num_reverse)-i-1], num_reverse[i]
        num_str_reverse = ''.join(num_reverse)

        """
        181130 Review 2

        Time : 20 min

        I like the code above which makes reversed number with str
        The way using list indexing below is slower

        """

        # 3)    (88 ms)
        # 181220 refactored with reverse index
        # num_str_reverse = num_str[::-1]

        if minus:
            result = int('-' + num_str_reverse)
        else:
            result = int(num_str_reverse)

        # 32-bit signed integer validation
        if result > 2**31-1 or result <= -2**31:
            return 0

        return result


if __name__ == '__main__':

    solution = Solution()
    print(solution.reverse(123))
    print(solution.reverse(-123))
    print(solution.reverse(120))
    print(solution.reverse(1534236469))
    print(solution.reverse(2147483648))
    print(solution.reverse(2200000000))  # -> exception case

    # print(int('000123'))
    # print(int('-000123'))
    # print(2**31-1)
    # print(-2**31)

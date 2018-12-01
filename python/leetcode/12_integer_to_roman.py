"""
12. Integer to Roman

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

"""
Time : 70 min

* Subject - Introducing new concept into coding test
* Learning
    1. Change the index when the order is reverse
        181201
        No need to change the index, just use list slicing (step) 
    
    2. Read carefully

"""


# I II III IV V VI VII VIII IX X


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        roman_str = ''

        for idx, i in enumerate(str(num)):
            idx = len(str(num)) - idx - 1
            if idx == 0:
                current_ten = 'I'   # 0
                current_five = 'V'  # 5
                next_ten = 'X'      # 10

            elif idx == 1:
                current_ten = 'X'   # 10
                current_five = 'L'  # 50
                next_ten = 'C'      # 100

            elif idx == 2:
                current_ten = 'C'   # 100
                current_five = 'D'  # 500
                next_ten = 'M'      # 1000

            # elif idx == 3:
            else:
                current_ten = 'M'   # 1000
                current_five = ''   # -
                next_ten = ''       # -

            i = int(i)
            if 1 <= i <= 3:
                roman_str = roman_str + (current_ten * i)

            if i == 4:
                roman_str = roman_str + (current_ten + current_five)

            if i == 5:
                roman_str = roman_str + current_five

            if 6 <= i <= 8:
                roman_str = roman_str + (current_five + current_ten * (i - 5))

            if i == 9:
                roman_str = roman_str + (current_ten + next_ten)

        return roman_str


if __name__ == '__main__':

    # input_data = 3
    # input_data = 4
    # input_data = 9
    # input_data = 58
    # input_data = 1994

    # Test
    input_data = 68
    # input_data = 500

    solution = Solution()
    print(solution.intToRoman(input_data))


"""

181201 Review

Time : 33 min

To rotate str list from the last index, the code above use this way.

    (1)
    for idx, i in enumerate(str(num)):
        idx = len(str(num)) - idx - 1

But, I found the better and simpler way using list slicing.

    (2)
    for idx, i in enumerate(str_num[::-1]):


"""



class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        def turn_int_to_roman(idx, i):

            if idx == 0:
                symbol_1 = 'I'
                symbol_5 = 'V'
                symbol_10 = 'X'

            elif idx == 1:
                symbol_1 = 'X'
                symbol_5 = 'L'
                symbol_10 = 'C'

            elif idx == 2:
                symbol_1 = 'C'
                symbol_5 = 'D'
                symbol_10 = 'M'

            else: # idx == 3:
                symbol_1 = 'M'
                symbol_5 = None
                symbol_10 = None

            roman_digit = ''

            if i < 4:
                roman_digit += symbol_1 * i

            elif i == 4:
                roman_digit += symbol_1 + symbol_5

            elif i == 5:
                roman_digit += symbol_5

            elif i < 9:
                roman_digit += symbol_5 + symbol_1 * (i - 5)

            elif i == 9:
                roman_digit += symbol_1 + symbol_10

            return roman_digit

        str_num = str(num)

        roman = ''
        for idx, i in enumerate(str_num[::-1]):
            result = turn_int_to_roman(idx, int(i))
            roman = result + roman

        return roman


if __name__ == '__main__':

    # input = 3
    # input = 4
    # input = 9
    # input = 58
    input = 68
    # input = 1994

    solution = Solution()
    print(solution.intToRoman(input))

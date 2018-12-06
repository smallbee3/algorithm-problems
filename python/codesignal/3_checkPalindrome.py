"""
3_checkPalindrome

Given the string, check if it is a palindrome.


Example

Given an array of integers, find the pair of adjacent elements
that has the largest product and return that product.

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;

For inputString = "abac", the output should be
checkPalindrome(inputString) = false;

For inputString = "a", the output should be
checkPalindrome(inputString) = true.

"""
"""
181205

Subject - Palindrome

Learning
    1. Compare string with reverse index
    2. The usage of 'reversed' method (but, reverse index is good enough

"""

def checkPalindrome1(inputString):

    # print(list(inputString))
    # print(list(reversed(inputString)))
    if list(inputString) == list(reversed(inputString)):
        return True
    else:
        return False


def checkPalindrome2(inputString):
    for i in range(len(inputString) // 2):
        if inputString[i] != inputString[len(inputString) - 1 - i]:
            return False
    return True


# The most simple way that I couldn't think about

def checkPalindrome(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False


# result = checkPalindrome('aabaa')
result = checkPalindrome('abacaba')
print(result)

"""
181205

Subject - Palindrome

Learning
    1. compare string with reverse index

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

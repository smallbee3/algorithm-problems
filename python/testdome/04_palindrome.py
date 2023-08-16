"""
4. Palindrome

A palindrome is a word that reads the same backward or forward.

Write a function that checks if a given word is a palindrome.
Character case should be ignored.

For example, is_palindrome("Deleveled") should return True
as character case should be ignored, resulting in "deleveled",
which is a palindrome since it reads the same backward and forward.


Time : 12.17 min
Tests: 3 pass / 0 fail
  Various words: Correct answer
  Example case: Correct answer
  Lowercase words: Correct answer

* Learning
    1. Slicing iterable data with step

"""


class Palindrome:
    # 1) len(list)
    # @staticmethod
    # def is_palindrome(word):
    #     word = word.lower()
    #     for i in range(len(word) // 2):
    #
    #         # print(i)
    #         # print(word[i])
    #         # print(len(word)-1-i)
    #         # print(word[len(word)-1-i])
    #
    #         if word[i] != word[len(word)-1-i]:
    #             return False
    #     return True

    # 181129
    # I like the answer with slicing
    # 2) Slicing
    @staticmethod
    def is_palindrome(word):
        word = word.lower()
        for i in range(len(word) // 2):
            # print(i)
            # print(word[i])
            # print(-(i+1))
            # print(word[-(i+1)])

            if word[i] != word[-(i + 1)]:
                return False
        return True


print(Palindrome.is_palindrome('Deleveled'))


"""
181111 Review

Time : 5.30 min
Tests: 3 pass / 0 fail
  Various words: Correct answer
  Example case: Correct answer
  Lowercase words: Correct answer
"""


# class Palindrome:
#
#     @staticmethod
#     def is_palindrome(word):
#         word = word.lower()
#         for i in range(len(word) // 2):
#             if word[i] != word[len(word)-i-1]:
#                 return False
#         return True
#
#
# print(Palindrome.is_palindrome('Deleveled'))


"""
230807 Review 2

Time: 8.19 min
Code: The same as ...
Mistake:
  Useless if statement because whether num_of_word is odd or even doesn't matter
        if num_of_word % 2 == 0:
            for i in range(num_of_word // 2):
                if word[i] != word[num_of_word - i - 1]:
                    return False

        else:
            for i in range(num_of_word // 2):
                if word[i] != word[num_of_word - i - 1]:
                    return False

"""

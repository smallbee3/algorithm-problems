"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""

"""
Time : 16 min

* Subject - Find common things among three objects 
* Learning
    1. Pseudo code
    2. Find common things among three objects
    
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        def find_common_prefix(a, b):
            common_str = ''
            short_length = len(a) if len(a) < len(b) else len(b)

            for i in range(short_length):
                if a[i] != b[i]:
                    break
                common_str += a[i]
            return common_str

        if not strs:
            return ""

        common = strs[0]
        for i in strs[1:]:
            common = find_common_prefix(common, i)

        return common if common else ""


if __name__ == '__main__':
    input = ["flower", "flow", "flight"]
    solution = Solution()
    print(solution.longestCommonPrefix(input))


"""

181130 Review 2

Time : 30 min

"""

# 181130
# The code above using inner function is easier to understand.
# It took too much time to write the code below.


class Solution:

    @classmethod
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        longest_str = strs[0]
        for str1 in strs[1:]:

            short_length = longest_str if len(longest_str) < len(str1) else str1
            common_str = ''

            for i in range(len(short_length)):
                if str1[i] != longest_str[i]:
                    break
                common_str += str1[i]

            # 181130
            # No need to compare, because the result itself is already longest_str
            # if len(longest_str) > len(common_str):
            longest_str = common_str

        if not longest_str:
            return ""
        return longest_str


Solution.longestCommonPrefix(["flower","flow","flight"])

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

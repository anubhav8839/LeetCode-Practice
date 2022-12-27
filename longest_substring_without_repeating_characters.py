#Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest 
substring
 without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        start=0
        end=0
        max_length=0
        while end<len(s):
            if s[end] in d and d[s[end]]>=start:
                start=d[s[end]]+1
            max_length=max(max_length,end-start+1)
            d[s[end]]=end
            end=end+1
        return max_length
'''
131. Palindrome Partitioning
Solved
Medium
Topics
Companies
Given a string s, partition s such that every 
substring
 of the partition is a 
palindrome
. Return all possible palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.

'''
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        stack = []
        def recurse(n,cur):
            if n == len(s):
                stack.append(cur[:])
            for i in range(n,len(s)):
                if(s[n:i+1] == s[n:i+1][::-1]):
                    cur.append(s[n:i+1])
                    recurse(i+1,cur)
                    cur.pop()
        recurse(0,[])
        return stack
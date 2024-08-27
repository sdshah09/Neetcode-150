'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

class Solution:
    def countFrequency(self,s):
        s1_dict = {}
        for i in s:
            if i not in s1_dict:
                s1_dict[i]=1
            else:
                s1_dict[i]+=1
        return s1_dict

    def minWindow(self, s: str, t: str) -> str:
        freq = self.countFrequency(t)
        i,j = 0,0
        minLength = float('inf')
        counter  = len(freq)
        string = ''
        while j<len(s):
            if s[j] in freq:
                freq[s[j]]-=1
                if freq[s[j]] == 0:
                    counter-=1
            while counter == 0:
                if (j-i+1)<minLength:
                    minLength = j-i+1
                    string = s[i:j+1]
                if s[i] in freq:
                    freq[s[i]]+=1
                    if freq[s[i]]>0:
                        counter+=1
                i+=1
            j+=1
        return string

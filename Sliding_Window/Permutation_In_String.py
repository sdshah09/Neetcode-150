'''
567. Permutation in String
Solved
Medium
Topics
Companies
Hint
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
915.3K
Submissions
2M
Acceptance Rate
44.7%

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for i in s1:
            if i not in s1_dict:
                s1_dict[i]=1
            else:
                s1_dict[i]+=1
        begin,end=0,0
        counter = len(s1_dict)
        while end<len(s2):
            if s2[end] in s1_dict:
                s1_dict[s2[end]]-=1
                if s1_dict[s2[end]]==0:
                    counter-=1
            end+=1
            while counter==0:
                if(end-begin)==len(s1):
                    return True
                if s2[begin] in s1_dict:
                    s1_dict[s2[begin]]+=1
                    if s1_dict[s2[begin]]>0:
                        counter+=1
                begin+=1
        return False
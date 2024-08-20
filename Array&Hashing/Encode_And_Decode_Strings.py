'''
String Encode and Decode
Solved 
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

'''
from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for i in strs:
            s+=str(len(i))+"#"+i
        return s
    def decode(self, s: str) -> List[str]:
        stack = []
        i = 0
        while i<len(s):
            if s[i].isdigit():
                j = i 
                while s[j]!="#":
                    j+=1
                length = int(s[i:j])
                i = j+1
                j = i+length
                stack.append(s[i:j])
                i = j
            else:
                i+=1
        return stack

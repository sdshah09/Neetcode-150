'''
78. Subsets
Solved
Medium
Topics
Companies
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = set()
        def recurse(index,cur):
            if len(cur)==len(nums):
                stack.add(tuple(cur[:]))
                return
            stack.add(tuple(cur[:]))
            for i in range(index,len(nums)):
                cur.append(nums[i])
                recurse(i+1,cur)
                cur.pop()
            return stack
        return recurse(0,[])
        
            
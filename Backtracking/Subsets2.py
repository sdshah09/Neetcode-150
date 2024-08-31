'''
90. Subsets II
Solved
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

'''
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        stack = set()
        nums.sort()
        def recurse(cur,index):
            stack.add(tuple(nums[i] for i in cur))
            for i in range(index,len(nums)):
                if i not in cur:
                    cur.append(i)
                    recurse(cur,i)
                    cur.pop()
            return stack
        return recurse([],0)

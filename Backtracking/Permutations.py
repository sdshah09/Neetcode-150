'''
46. Permutations
Solved
Medium
Topics
Companies
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.

'''

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack = []
        def recurse(cur):
            if len(cur) == len(nums):
                stack.append(cur[:])
                return
            for i in range(len(nums)):
                if nums[i] not in cur:
                    cur.append(nums[i])
                    recurse(cur)
                    cur.pop()
            return stack
        return recurse([])
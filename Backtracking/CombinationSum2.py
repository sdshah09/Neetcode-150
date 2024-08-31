'''
40. Combination Sum II
Solved
Medium
Topics
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''

from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        stack = set()
        def recurse(cur,summ,index):
            if summ<0:
                return 
            if summ == 0:
                stack.add(tuple(candidates[i] for i in cur))
                return
            for i in range(index,len(candidates)):
                if i>index and candidates[i]==candidates[i-1]:  # To skip duplicates keep this in mind because you forget this 
                    continue
                cur.append(i)
                recurse(cur,summ-candidates[i],i+1)
                cur.pop()
            return stack
        return recurse([],target,0)
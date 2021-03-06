"""
Medium 198. House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400

"""
class Solution:        
    def rob(self, nums: List[int]) -> int:
        """
        dp improved - two values
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        val1, val2 = 0, nums[0]
        for i in range(1,n):
            tmp = val2
            val2 = max(val1 + nums[i], val2)
            val1 = tmp
        return val2
         
#     def rob(self, nums: List[int]) -> int:
#         """
#         dp
#         """
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         nums.insert(0, 0)
#         for i in range(2,n+1):
#             nums[i] = max(nums[i-2] + nums[i], nums[i-1])
#         return nums[-1]
            
#  ## dfs: time out
#     def dfs(self, nums, i, memo):
#         if i < 0:
#             return 0
#         if memo[i] > 0:
#             return memo[i]
#         res =  max(self.dfs(nums, i-2, memo) + nums[i], self.dfs(nums, i-1, memo))
#         memo[i] = res
#         return memo[i]

#     def rob(self, nums: List[int]) -> int:
#         """
#         recursion + memo -- timeout
#         """
#         n = len(nums)
#         return self.dfs(nums, n-1, [0]*n)    
"""
very nice explanation:
https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
"""
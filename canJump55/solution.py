from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach_index = 0
        for i in range(len(nums)):
            if i > max_reach_index:
                return False
            max_reach_index = max(max_reach_index, i + nums[i])
        return True

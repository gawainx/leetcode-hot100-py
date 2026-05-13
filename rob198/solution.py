from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        dp_arr = [0 for _ in range(length + 1)]
        for i in range(length + 1):
            if i == 0:
                continue
            if i == 1:
                dp_arr[i] = nums[i - 1]
            else:
                dp_arr[i] = max(dp_arr[i - 2] + nums[i - 1], dp_arr[i - 1])
        return dp_arr[-1]
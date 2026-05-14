from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        length = len(uniq_nums)
        result = 0
        for num in uniq_nums:
            if num - 1 in uniq_nums:
                continue

            curr_length = 1
            for i in range(1, length):
                if num + i in uniq_nums:
                    curr_length += 1
                else:
                    break

            result = max(result, curr_length)
        return result

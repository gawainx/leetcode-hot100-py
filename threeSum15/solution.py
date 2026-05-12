class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results = list()
        sorted_num = list(sorted(nums))
        length = len(nums)
        prev_value = None
        for idx, num in enumerate(sorted_num):
            if prev_value is not None and prev_value == num:
                continue
            i = idx + 1
            j = length - 1
            while i < j:
                temp_result = num + sorted_num[i] + sorted_num[j]
                if temp_result > 0:
                    j = j - 1
                elif temp_result < 0:
                    i = i + 1
                else:
                    results.append([num, sorted_num[i], sorted_num[j]])
                    next_j = j - 1
                    while (sorted_num[next_j] == sorted_num[j]) and next_j > i:
                        next_j = next_j - 1
                    next_i = i + 1
                    while (sorted_num[next_i] == sorted_num[i]) and next_i < j:
                        next_i = next_i + 1
                    i = next_i
                    j = next_j
            prev_value = num
        return results

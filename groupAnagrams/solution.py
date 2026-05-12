from typing import List

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings = defaultdict(list)
        for word in strs:
            mappings["".join(sorted(word))].append(word)
        results = []
        for k, v in mappings.items():
            results.append(v)
        return results

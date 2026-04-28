class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        new = Counter(nums)
        n = len(nums)
        for key in new:
            if new[key] > n/2:
                return key
        
        
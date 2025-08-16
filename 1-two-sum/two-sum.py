class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for k,v in enumerate(nums):
            m=target-v
            if m in d:
                return [d[m], k]
            d[v]=k
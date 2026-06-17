class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        sumo=(n*(n+1))//2
        num=sumo-sum(nums)
        return num        
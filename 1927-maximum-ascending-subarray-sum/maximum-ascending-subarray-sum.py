class Solution(object):
    def maxAscendingSum(self, nums):
        maxsum=nums[0]
        cursum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                cursum+=nums[i]
            else:
                cursum=nums[i]
            if cursum>maxsum:
                maxsum=cursum
        return maxsum                
        
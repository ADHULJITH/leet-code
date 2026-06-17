class Solution(object):
    def intersection(self, nums1, nums2):
        l1=set(nums1)
        l2=set(nums2)
        return list(l1&l2)
        
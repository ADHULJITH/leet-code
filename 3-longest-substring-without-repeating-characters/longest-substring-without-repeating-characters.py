class Solution(object):
    def lengthOfLongestSubstring(self, s):
        d=set()
        l=0
        max_len=0
        for r in range(len(s)):
            while s[r] in d:
                d.remove(s[l])
                l+=1
            d.add(s[r])
            if r-l+1>max_len:
                max_len=r-l+1
        return max_len            
        
class Solution(object):
    def lengthOfLastWord(self, s):
        k=s.split()
        c=k[len(k)-1]
        return len(c)
        
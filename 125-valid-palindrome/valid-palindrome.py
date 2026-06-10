class Solution(object):
    def isPalindrome(self, s):
        l=""
        for i in s:
            if i.isalnum():
                l+=i.lower()
        if l==l[::-1]:
            return True
        else:
            return False          
    
        
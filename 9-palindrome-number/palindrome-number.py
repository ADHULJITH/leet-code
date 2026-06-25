class Solution(object):
    def isPalindrome(self, x):
        rev=0
        if x<0:
            return False
        else:
            temp=x
            while temp!=0:
                digi=temp%10
                rev=rev*10+digi
                temp//=10  
            if rev==x:
                return True
            else:
                return False            
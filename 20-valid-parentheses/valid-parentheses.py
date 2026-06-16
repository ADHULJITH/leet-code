class Solution(object):
    def isValid(self, s):
        d={'}':'{',']':'[',')':'('}
        stack=[]
        for i in s:
            if i in '{([':
                stack.append(i)
            else:
                if not stack or stack.pop()!=d[i]:
                    return False
                         
        return len(stack)==0        
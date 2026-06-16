class Solution(object):
    def moveZeroes(self, num):
        r=[]
        k=0
        for i in range(len(num)):
            if num[i]!=0:
                num[i],num[k]=num[k],num[i]
                k+=1
        return num       

        
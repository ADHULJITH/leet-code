class Solution(object):
    def plusOne(self, digits):
        d="".join(map(str,digits))
        nm=int(d)+1
        return list(map(int, str(nm)))
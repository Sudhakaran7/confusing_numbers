class Solution(object):
    def confusingNumber(self, N):
        """
        :type N: int
        :rtype: bool
        """
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        
        S = str(N)
        for i in range(len(S)):
            if S[i] not in lookup:
                return False
        for i in range((len(S)+1)//2):
            if S[i] != lookup[S[-(i+1)]]:
                return True
        return False
val=Solution()
n=int(input())
print(val.confusingNumber(n))

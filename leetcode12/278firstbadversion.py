import math
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    return version>=3

class Solution:
    def firstBadVersion(n):
        """
        :type n: int
        :rtype: int
        """
        minN,maxN,midP,x=1,n,int(round(n/2)),0
        
        if n==1:
            return 1

        while x<n:
            if isBadVersion(midP):
                maxN=midP
                if maxN==midP and minN==midP:
                    return midP
                midP=int((maxN+minN)/2)
            else:
                minN=midP+1
                if minN==midP:
                    return midP
                midP=int((minN+maxN)/2)
            x+=1
        return midP

print(Solution.firstBadVersion((3)))
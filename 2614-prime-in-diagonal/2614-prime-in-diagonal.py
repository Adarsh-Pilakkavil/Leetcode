class Solution(object):
    def diagonalPrime(self, nums):
        l=[]
        c=0
        k=0
        for i in range(0,len(nums),1):
            l.append(nums[i][i])
            l.append(nums[i][len(nums)-i-1])
        for i in l:
            if i>k:
                for j in range(2,i//2,1):
                    if i%j==0:
                        c+=1
                        break
                if i==1:
                    c+=1
                if c>0:
                    c=0
                else:
                    if i>k:
                        k=i
                        c=0
                    else:
                        c=0
        return k

        
        
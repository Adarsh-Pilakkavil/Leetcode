class Solution(object):
    def findWordsContaining(self, words, x):
        z=0;
        lis=[]
        for i in words:
            if x in i:
                lis.append(z)
            z+=1;
        return lis;
class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        ans=""
        z=0
        for i in  range(0,len(word),1):
            if word[i]==ch:
                z=i
                break
        for i in range(z,-1,-1):
            ans+=word[i]
        for i in range(z+1,len(word),1):
            ans+=word[i]
        return ans
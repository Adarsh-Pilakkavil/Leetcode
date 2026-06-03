class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        l=[]
        if len(groups)==1:
            return words
        c=1-groups[0]
        l.append(words[0])
        for i in range(1,len(words)):
            if groups[i]==c:
                c=1-c
                l.append(words[i])
        return l
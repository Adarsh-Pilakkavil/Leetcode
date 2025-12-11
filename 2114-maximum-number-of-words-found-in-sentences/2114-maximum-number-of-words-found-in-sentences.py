class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        z=0
        for i in sentences:
            if i.count(" ")+1>z:
                z=i.count(" ")+1
        return z
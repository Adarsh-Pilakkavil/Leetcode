class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1
        return haystack.find(needle)
        
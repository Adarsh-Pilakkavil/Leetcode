class Solution(object):
    def trailingZeroes(self, n):
        return n//3125+n//625+n//125+n//25+n//5
            
class Solution(object):
    def findClosest(self, x, y, z):
        if abs(z-x)>abs(z-y):
            return 2
        elif abs(z-x)<abs(z-y):
            return 1
        else:
            return 0
        
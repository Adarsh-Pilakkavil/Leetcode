class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        k1=(ord(coordinate1[0])-96)+int(coordinate1[1])
        k2=(ord(coordinate2[0])-96)+int(coordinate2[1])
        if (k1%2==0 and k2%2==0) or (k1%2==1 and k2%2==1):
            return True
        else:
            return False
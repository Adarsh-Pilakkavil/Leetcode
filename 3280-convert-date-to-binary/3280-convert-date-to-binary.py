class Solution(object):
    def convertDateToBinary(self, date):
        return bin(int(date[0:4:1]))[2:]+"-"+bin(int(date[5:7]))[2:]+"-"+bin(int(date[8:10:1]))[2:]
        
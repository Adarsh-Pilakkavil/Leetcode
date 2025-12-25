class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        l=-1
        for i in s.split():
            if i[0].isdigit():
                if int(i)<=l:
                    return False
                l=int(i)
        return True
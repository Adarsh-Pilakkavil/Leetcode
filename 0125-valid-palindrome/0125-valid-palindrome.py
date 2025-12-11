class Solution(object):
    def isPalindrome(self, s):
        k=""
        for i in s:
            if i.isalnum():
                k+=i
        k=k.lower()
        if k[::-1]==k:
            return True
        else:
            return False
        
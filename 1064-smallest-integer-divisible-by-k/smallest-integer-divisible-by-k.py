class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length
        
        return -1
        
#If a number has remainder r when divided by k, then:
# number = k * q + r
# Now, when you append a 1 to the number:
# new_number = number * 10 + 1
# Its remainder mod k is:
# (new_number % k) = (number % k * 10 + 1) % k
#                  = (r * 10 + 1) % k
# This lets you build the remainder, without building the number.
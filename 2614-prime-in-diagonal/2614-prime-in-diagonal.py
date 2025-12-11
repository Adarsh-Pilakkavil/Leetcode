class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num <=1:
                return False
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    return False
            return True
        biggest_prime = 0
        length = len(nums)
        for i in range(length):
            if nums[i][i] > biggest_prime:
                if isPrime(nums[i][i]):
                    biggest_prime = nums[i][i]
            if nums[i][length-i-1] > biggest_prime:
                if isPrime(nums[i][length-i-1]):
                    biggest_prime = nums[i][length-i-1]

        return biggest_prime
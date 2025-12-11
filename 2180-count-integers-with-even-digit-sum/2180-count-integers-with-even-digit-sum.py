class Solution:
    def countEven(self, num: int) -> int:
        s = sum(int(d) for d in str(num))
        if s % 2 == 0:
            return num // 2
        return (num - 1) // 2
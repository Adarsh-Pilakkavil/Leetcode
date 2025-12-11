class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_h = heights
        sorted_h = sorted(heights)

        idx = 0
        cnt = 0
        for n in heights:
            if(n != sorted_h[idx]):
                cnt += 1
            idx += 1
            
        return cnt
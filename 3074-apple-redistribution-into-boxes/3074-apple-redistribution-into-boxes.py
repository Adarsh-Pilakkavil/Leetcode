class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        totalapple=sum(apple)
        capacity.sort(reverse=True)
        count=0
        while totalapple>0 and count<len(capacity):
            totalapple-=capacity[count]
            count+=1
        return count

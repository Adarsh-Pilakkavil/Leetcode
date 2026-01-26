class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        l=[]
        c=10**10
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i])<c:
                l=[]
                l.append([min(arr[i],arr[i+1]),max(arr[i],arr[i+1])])
                c=abs(arr[i+1]-arr[i])
            elif abs(arr[i+1]-arr[i])==c:
                l.append([min(arr[i],arr[i+1]),max(arr[i],arr[i+1])])
        return l
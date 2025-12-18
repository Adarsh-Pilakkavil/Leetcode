class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        c=3000
        s=[]
        for i in range(len(list1)):
            if list1[i] in list2:
                j=list2.index(list1[i])
                if i+j<c:
                    s=[list1[i]]
                    c=i+j
                elif i+j==c:
                    s.append(list1[i])
                else:
                    continue
        return s
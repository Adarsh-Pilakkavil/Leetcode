class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i=1
        while i<=memory2 or i<=memory1:
            if memory1>=memory2 and memory1>=i:
                memory1-=i
                i+=1
            elif memory2>=memory1 and memory2>=i:
                memory2-=i
                i+=1
            else:
                break
        return [i,memory1,memory2]
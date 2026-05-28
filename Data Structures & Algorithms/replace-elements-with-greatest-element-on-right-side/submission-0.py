class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        
        for i in range(n):
            arr[i] = max(arr[i+1:],default=-1)
        return arr



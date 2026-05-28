class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res =temp=0
        for i in range(len(nums)):
            if nums[i]==1:
                temp +=1
                res = max(res,temp)
            else:
                temp=0
        return res

            
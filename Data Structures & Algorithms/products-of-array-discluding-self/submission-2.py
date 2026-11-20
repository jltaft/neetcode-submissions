class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        suff = [0] * n
        res = [0] * n

        #nothing left of index 0
        pre[0] = 1
        #nothing right of last index
        suff[n-1] = 1 

        #build prefix products
        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i-1]

        #build suffix products
        for i in range(n-2,-1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        #build result
        for i in range(n):
            res[i] = pre[i] * suff[i]
       
        return res

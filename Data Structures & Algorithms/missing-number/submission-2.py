class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_list = nums.copy()
        for i in range(len(nums)+1):
            if i not in num_list:
                return i
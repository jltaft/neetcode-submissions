class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracker = {}

        for i in nums:
            #if number is already in dict
            if i in tracker.keys():
                tracker[i]  += 1
            #if number is not in dict
            else:
                tracker[i]= 1

        for key, value in tracker.items():
            if value == 1:
                return key


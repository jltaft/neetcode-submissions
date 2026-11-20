class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        #dict of number frequencies
        for i in nums:
            if i in freq.keys():
                freq[i] += 1
            else:
                freq[i] = 1
    
        #sort through dict to find top k-th
        freqsort = list(sorted(freq.items(), key=lambda item: item[1]))

        res = []
        while len(res) < k:
            res.append(freqsort.pop()[0])
        return res
        
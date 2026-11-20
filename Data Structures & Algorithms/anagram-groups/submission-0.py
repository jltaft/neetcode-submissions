class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #to determine anagrams
        d = {}

        for i in strs:
            sort = "".join(sorted(i))
            if sort not in d.keys():
                d[sort] = [i]
            else:
                d[sort].append(i)
        
        return list(d.values())
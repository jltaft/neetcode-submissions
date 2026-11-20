from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters1 = {}
        characters2 = {}

        for i in s:
            if i in characters1.keys():
                characters1[i] += 1
            else: 
                characters1[i] = 1
        
        for i in t:
            if i in characters2.keys():
                characters2[i] += 1
            else: 
                characters2[i] = 1

        if characters1 == characters2:
            return True
        else:
            return False
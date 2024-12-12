"Time Complexity is O(N)"
"Space Complexity is O(1)"

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lenofp = len(p)
        p1 = sorted(p)
        result = []

        for i in range(len(s)-lenofp+1):
            stringtomatch = s[i:i+lenofp]
            if sorted(stringtomatch) == p1:
                result.append(i)
        
        return result

        
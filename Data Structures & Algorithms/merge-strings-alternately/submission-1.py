class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        l1 = len(word1)
        l2 = len(word2)
        c2=0
        for i in range(l1):
            merged+=word1[i]

            if l2 > 0:
                c2+=1
                l2-=1
                merged+=word2[i]
        
        if l2>0:
            merged+=word2[c2:]
        return merged


       
            
        
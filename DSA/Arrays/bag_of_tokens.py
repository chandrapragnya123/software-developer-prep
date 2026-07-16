class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        maxi = 0 
        l = 0 
        r = len(tokens)-1 
        while l <= r:
            if tokens[l] <= power:
                power = power - tokens[l]
                l += 1 
                score += 1 
                maxi = max(maxi,score)
            elif score > 0:
                power = power+ tokens[r] 
                r -= 1
                score  -= 1
            else:
                break  
        return maxi
        

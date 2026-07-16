class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        c = 0 
        l = 0 
        r = len(people)-1 
        while l <= r :
            if people[l] + people[r] > limit:
                c += 1
                r -= 1 
            else:
                c += 1 
                l += 1
                r -= 1 
        return c  

        

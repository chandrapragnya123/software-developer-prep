class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 1_000_000_007
        nums.sort()
        ans = 0 
        l = 0 
        r = len(nums)-1 
        while l <= r:
            if nums[l]+nums[r] <= target:
                ans = (ans + pow(2,r-l,MOD)) % MOD 
                l += 1 
            else:
                r -= 1 
        return ans 
        

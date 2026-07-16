class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p1 = 0 
        p2 = len(nums) - 1 
        idx = len(nums) - 1 
        nums1 = [0]*n
        while p1 <= p2:
            e1 = nums[p1]**2 
            e2 = nums[p2]**2 
            if e1 > e2:
                nums1[idx] = e1
                p1 += 1 
            else:
                nums1[idx] = e2
                p2 -= 1 
            idx -= 1 
        return nums1

        

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i-1] == nums[i]:
                continue 
            for j in range(i+1,len(nums)-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue 
                left = j+1
                right = len(nums)-1 
                
                while left < right:
                    sums = nums[i]+nums[j]+nums[left]+nums[right]
                    if(sums == target):
                        res.append((nums[i],nums[j],nums[left],nums[right]))
                        left += 1 
                        right -= 1 
                        while left < right and nums[left-1] == nums[left]:
                            left += 1 
                        while left < right and nums[right +1] == nums[right]:
                            right -= 1 
                    elif (sums > target):
                        right -= 1 
                    else:
                        left += 1 
        return res

        

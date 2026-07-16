class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                sums = nums[i] + nums[l] + nums[r]

                if abs(target - sums) < abs(target - closest):
                    closest = sums

                if sums < target:
                    l += 1
                elif sums > target:
                    r -= 1
                else:
                    return sums

        return closest

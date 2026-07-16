class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        nums.sort()

        for i in range(len(nums) - 2):

            l = i + 1
            r = len(nums) - 1

            while l < r:

                sums = nums[i] + nums[l] + nums[r]

                if sums == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif sums < 0:
                    l += 1

                else:
                    r -= 1

        return [list(x) for x in result]

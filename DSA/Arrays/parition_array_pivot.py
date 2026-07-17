class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        res = [0] * len(nums)
        idx = 0

        # First pass: elements < pivot
        for num in nums:
            if num < pivot:
                res[idx] = num
                idx += 1

        # Second pass: elements == pivot
        for num in nums:
            if num == pivot:
                res[idx] = num
                idx += 1

        # Third pass: elements > pivot
        for num in nums:
            if num > pivot:
                res[idx] = num
                idx += 1

        return res
        

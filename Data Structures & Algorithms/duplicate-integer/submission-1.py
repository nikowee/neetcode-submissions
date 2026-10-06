class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        nums.sort()
        prev = nums[0]

        for num in nums[1:]:
            if num == prev:
                return True
            prev = num

        return False

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Stores remainder:index pairs
        remainders = {}

        for i, val in enumerate(nums):
            # If the value at i matches one of the remainders we are looking for, return
            if val in remainders:
                return [remainders.get(val), i]
            
            # If not then find remainder of value at i and add to store
            remainders[target - val] = i


            
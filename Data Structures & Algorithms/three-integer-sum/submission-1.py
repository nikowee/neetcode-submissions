class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, val_i in enumerate(nums):
            # if val_i is > 0 then no combination of larger numbers will make sum of zero
            if val_i > 0:
                break
            
            # If val_i is a duplicate of the previous i's value then the answer will be the same so skip
            if i > 0 and val_i == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                sum = val_i + nums[left] + nums[right]

                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else: 
                    output.append([val_i, nums[left], nums[right]])
                    
                    # Move both left and right inwards 
                    # If we only move one in, sum only == 0 if that one is a duplicate which we dont want
                    left += 1
                    right -= 1
                    # Check if new left is duplicate and shift until not
                    while nums[left] == nums[left-1] and left < right:
                        left += 1

        return output
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        array = sorted(nums)

        for i, val_i in enumerate(array):
            left, right = i+1, len(array)-1
            
            while left < right:
                sum = val_i + array[left] + array[right]

                if sum == 0:
                    new_entry = [val_i, array[left], array[right]]
                    if new_entry not in output:
                        output.append(new_entry)
                        continue
                elif sum > 0:
                    right -= 1
                    continue
                
                # If sum < 0 OR if sum == 0 and distinct
                left += 1

        return output
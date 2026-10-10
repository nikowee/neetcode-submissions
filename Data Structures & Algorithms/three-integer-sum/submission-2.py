class Solution:
    # Time complexity: O(n^4) worst case if all the triplets found are the same
    # This is caused by the "if new_entry not in output:" check
    # Space complexity: O(n)

    # n is the number of elements in the input nums
    # output stores the list of unique triplets
    # array is the sorted version of nums

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

                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                    continue
                else: 
                    left += 1

        return output
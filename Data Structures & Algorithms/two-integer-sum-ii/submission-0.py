class Solution:
    # 2 pointer convergence
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        # Start from leftmost and rightmost index and stop when the 2 pointers cross
        while left < right:
            # Found target
            sum = numbers[left] + numbers[right]
            if  sum == target:
                return [left+1, right+1]
            # Did not find target
            elif sum > target:
                right -= 1
            else: 
                left += 1
            
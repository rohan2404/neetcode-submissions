class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L, R = 0, n-1
        while L < R:
            left = numbers[L]
            right = numbers[R]
            if left + right > target:
                R -= 1
            if left + right < target:
                L += 1
            if left + right == target:
                return [L+1, R+1]
        
                
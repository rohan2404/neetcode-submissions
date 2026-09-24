class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        L, R = 0, n-1
        def calcArea(l, r):
            width = r-l
            height = min(heights[l], heights[r])
            return width * height
        best = 0
        while L < R:
            currArea = calcArea(L,R)
            best = max(best, currArea)
            if heights[L] <= heights[R]:
                L += 1
            else:
                R -= 1

        return best
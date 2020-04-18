class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        i,j = 0, len(height)-1
        while i<j:
            if height[i]<height[j]:
                maxwater = max(maxwater,(j-i) * height[i])
                i+=1
            else:
                maxwater = max(maxwater,(j-i) * height[j])
                j-=1

        return maxwater

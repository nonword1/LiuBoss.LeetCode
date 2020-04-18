class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        count = 0
        for i in range(l):
            index = l-1-i
            if nums[index] ==0:
                count +=1
                nums[index:l-count] = nums[index+1:l-count+1]
                nums[l-count] =0
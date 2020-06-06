class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        cnt = 0
        lcnt = 0
        for i in nums:
            if i in num_set:
                cnt = 0
                left = i 
                right = i + 1
                while left in num_set:
                    cnt += 1
                    num_set.remove(left)
                    left -= 1
                while right in num_set:
                    cnt += 1
                    num_set.remove(right)
                    right += 1
                lcnt = max(lcnt,cnt)
        return lcnt

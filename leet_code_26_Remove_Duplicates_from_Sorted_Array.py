class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] = '$'
        while len(nums) and '$' in nums:
            nums.remove('$')
        return len(nums)
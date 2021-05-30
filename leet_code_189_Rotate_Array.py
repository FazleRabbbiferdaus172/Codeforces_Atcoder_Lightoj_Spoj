class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = k % len(nums)
        nums[:] = nums[-x:]+nums[:-x]
        print(nums)
        return nums
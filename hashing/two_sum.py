class Solution():
    def twoSum(self, nums, target):
        seen = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            else:
                seen[nums[i]] = i


nums = [2,7,6,5]
target = 9
c = Solution()
print(c.twoSum(nums,target))
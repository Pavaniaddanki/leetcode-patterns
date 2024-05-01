# Pattern:     Hashset
# Brute force: We check if each member of the array is duplicate or not, O(n2) time / O(?) space
# Optimized:   Hashset, O(n) time / O(?) space
# Trade-off:   <what the optimized version gives up, and when I'd choose differently>
#
# Key insight: <one sentence, in my own words>
# Edge cases:  <empty input, negatives, duplicates, ...>

class Solution():
    def contains_duplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]):
                    return True
        return False

    def containsDuplicate(self,nums):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
               seen.add(nums[i])
        return False

nums = [1,2,3,1]
c = Solution()
#print(c.contains_duplicate(nums))
print(c.containsDuplicate(nums))

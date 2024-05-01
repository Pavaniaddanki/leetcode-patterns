# <number>. <Title> — https://leetcode.com/problems/<slug>/
# Pattern:     <pattern name>
# Brute force: <idea>, O(?) time / O(?) space
# Optimized:   <idea>, O(?) time / O(?) space
# Trade-off:   <what the optimized version gives up, and when I'd choose differently>
#
# Key insight: <one sentence, in my own words>
# Edge cases:  <empty input, negatives, duplicates, ...>

from typing import List


class Solution:
    def brute_force(self, nums: List[int]) -> int:
        pass

    def solve(self, nums: List[int]) -> int:   # rename to LeetCode's method name
        pass


if __name__ == "__main__":
    s = Solution()
    tests = [
        # (input, expected),
    ]
    for args, expected in tests:
        for name in ("brute_force", "solve"):
            got = getattr(s, name)(args)
            status = "ok  " if got == expected else "FAIL"
            print(f"{status} {name}({args}) = {got}, expected {expected}")

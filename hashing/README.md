# Hashing

**Idea:** Walk the array once and remember what you've seen in a set or dict, so "have I seen X?" costs O(1) instead of another loop.

**Recognize it when:** brute force compares every pair (O(n²)), and the condition can be rewritten as "I need exactly value Y."

**Set or dict?**
- Set → only need to know *seen or not* (Contains Duplicate)
- Dict → need *where* (index) or *how many* (count) (Two Sum, Subarray Sum = K)

**Order matters:** check first, then add, or an element will match itself.

**Trade-off to mention:** O(n) extra space. If the input is sorted (or can be sorted), two pointers give O(1) space.

| # | Problem | File |
|---|---|---|
| 217 | Contains Duplicate | `0217_contains_duplicate.py` |
| 1 | Two Sum | `0001_two_sum.py` |

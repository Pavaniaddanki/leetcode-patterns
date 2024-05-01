# Two Pointers

**Idea:** Put one pointer at each end and move them toward each other, using a rule that safely discards one option per step.

**Recognize it when:** the input is sorted (or can be sorted), and you're looking for pairs/triplets or the best pair from both ends.

**Trade-off to mention:** O(1) extra space versus a hash map's O(n), but sorting costs O(n log n) and loses the original indices.

| # | Problem | File |
|---|---|---|
| 15 | 3Sum | `0015_3sum.py` |
| 11 | Container With Most Water | `0011_container_with_most_water.py` |

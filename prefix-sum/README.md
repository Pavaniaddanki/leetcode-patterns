# Prefix Sum

**Idea:** A prefix sum is the running total up to each position. The sum of any subarray is the difference of two running totals:

`sum(i..j) = prefix[j] - prefix[i-1]`

**Prefix sum + hash map:** to count subarrays summing to `k`, ask at each step "how many earlier totals equal `current - k`?" That's Two Sum on running totals.

**Why not sliding window?** Sliding window needs all values ≥ 0 so that growing the window always increases the sum. With negatives there is no valid shrink rule.

**What does the map store?**
- Count of each total → "how many subarrays"
- First index of each total → "longest subarray"

**Don't forget:** start the map with `{0: 1}` (the empty prefix).

| # | Problem | File |
|---|---|---|
| 238 | Product of Array Except Self | `0238_product_of_array_except_self.py` |
| 560 | Subarray Sum Equals K | `0560_subarray_sum_equals_k.py` |

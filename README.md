# LeetCode Patterns

My solutions to LeetCode problems, organized by **pattern** rather than by problem number.

For each problem I write the brute force first, then the optimized version, and record the trade-off between them.

## How each solution is written

Every file starts with a header:

```python
# <number>. <title> — <link>
# Pattern:     <pattern name>
# Brute force: <idea>, <time> / <space>
# Optimized:   <idea>, <time> / <space>
# Trade-off:   <what I gave up, and when I'd choose differently>
```

See [`TEMPLATE.py`](TEMPLATE.py).

## Patterns

| Folder | Pattern | Recognize it when… |
|---|---|---|
| [`hashing/`](hashing/) | Hash set / hash map lookup | Brute force checks every pair, and you can turn the check into "have I seen X before?" |
| [`prefix-sum/`](prefix-sum/) | Running totals (+ hash map) | You need subarray sums, especially when negatives are allowed |
| [`kadane/`](kadane/) | Best subarray ending here | "Maximum/minimum subarray" questions |
| [`binary-search/`](binary-search/) | Halve the search space | Sorted (or rotated sorted) input, and O(log n) is expected |
| [`two-pointers/`](two-pointers/) | Pointers moving toward each other | Sorted input, pairs/triplets, or shrinking from both ends |

## Progress — Blind 75: Arrays

| # | Problem | Difficulty | Pattern | Status |
|---|---|---|---|---|
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Easy | hashing | ⬜ |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | hashing | ⬜ |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | kadane | ⬜ |
| 238 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | prefix-sum | ⬜ |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Medium | kadane | ⬜ |
| 152 | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Medium | kadane | ⬜ |
| 153 | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Medium | binary-search | ⬜ |
| 33 | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Medium | binary-search | ⬜ |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | two-pointers | ⬜ |
| 11 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Medium | two-pointers | ⬜ |

## Other problems

| # | Problem | Difficulty | Pattern | Status |
|---|---|---|---|---|
| 560 | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) | Medium | prefix-sum | 🟨 brute force done |

Legend: ⬜ not started · 🟨 in progress · ✅ done

## Running a solution

Each file runs on its own and checks itself with a few test cases:

```bash
python hashing/0217_contains_duplicate.py
```

Problem statements belong to LeetCode, so each file links to the problem instead of copying it.

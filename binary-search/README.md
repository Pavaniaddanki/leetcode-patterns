# Binary Search

**Idea:** Repeatedly cut the search space in half by checking the middle and deciding which half can still hold the answer.

**Recognize it when:** the input is sorted (or rotated sorted), or the problem expects O(log n).

**Rotated arrays:** at least one half around `mid` is always sorted. Work out which half it is, then check whether the target falls inside it.

| # | Problem | File |
|---|---|---|
| 153 | Find Minimum in Rotated Sorted Array | `0153_find_minimum_in_rotated_sorted_array.py` |
| 33 | Search in Rotated Sorted Array | `0033_search_in_rotated_sorted_array.py` |

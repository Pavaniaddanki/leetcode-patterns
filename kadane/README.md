# Kadane's Algorithm

**Idea:** For each position, keep the best answer for a subarray that *ends here*. Either extend the previous subarray or start fresh at the current element.

**Recognize it when:** "maximum (or minimum) sum/product of a contiguous subarray," or a running best that resets when it stops helping.

| # | Problem | File |
|---|---|---|
| 121 | Best Time to Buy and Sell Stock | `0121_best_time_to_buy_and_sell_stock.py` |
| 53 | Maximum Subarray | `0053_maximum_subarray.py` |
| 152 | Maximum Product Subarray | `0152_maximum_product_subarray.py` |

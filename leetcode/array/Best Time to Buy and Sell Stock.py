from typing import List


def main():
    so = Solution()
    print(so.maxProfit([7, 1, 5, 3, 6, 4]))


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = float("-inf")

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == '__main__':
    main()

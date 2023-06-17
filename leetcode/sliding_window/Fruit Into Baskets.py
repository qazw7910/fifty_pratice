from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start = 0
        curr_fruits = 0
        max_fruits = 0
        basket = {}

        for end in range(len(fruits)):
            curr_fruits += 1
            basket[fruits[end]] = basket.get(fruits[end], 0) + 1

            while len(basket) > 2:
                curr_fruits -= 1
                basket[fruits[start]] -= 1

                if basket[fruits[start]] == 0:
                    del basket[fruits[start]]

                start += 1

        max_fruits = max(max_fruits, curr_fruits)

        return max_fruits


if __name__ == '__main__':
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    so = Solution()
    print(so.totalFruit(fruits))

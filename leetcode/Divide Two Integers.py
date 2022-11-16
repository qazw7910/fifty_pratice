def main():
    so = Solution()
    print(so.divide(dividend=7, divisor=-3))


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend > 0) is (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        if dividend < divisor:
            return res

        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend >= tmp:
                dividend -= tmp
                res += 1
                i <<= 1
                tmp <<= 1

        if not positive:
            res = -res

        return min(max(-2147483648, res), 2147483647)


if __name__ == '__main__':
    main()

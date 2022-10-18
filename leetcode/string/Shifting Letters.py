def main():
    so = Solution()
    print(so.shiftingLetters(s="abc", shifts=[3, 5, 9]))


class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        sumi = sum(shifts)
        L = list(map(ord, s))
        for i in range(len(L)):
            L[i] = (L[i] - ord('a') + sumi) % 26 +ord('a')
            sumi -= shifts[i]
        return ''.join(map(chr, L))


if __name__ == '__main__':
    main()

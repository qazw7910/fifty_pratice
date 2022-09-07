def main():
    so = Solution()
    print(so.convert(s="PAYPALISHIRING", numRows=3))


class Solution(object):
    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s

        L = [''] * numRows

        index, step = 0, 1
        for i in s:
            L[index] += i
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)


if __name__ == '__main__':
    main()

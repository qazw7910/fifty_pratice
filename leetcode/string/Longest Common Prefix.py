def main():
    so = Solution()
    print(so.longestCommonPrefix(strs=["flower", "flow", "flight"]))


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pre = ""

        for t in zip(*strs):
            if len(set(t)) == 1:
                pre += t[0]
            else:
                break
        return pre

if __name__ == '__main__':
    main()

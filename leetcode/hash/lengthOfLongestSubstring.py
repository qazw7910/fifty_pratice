def main():
    so = Solution()
    print(so.lengthOfLongestSubstring("abcabcbb"))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return len(s)

        fast = 0
        slow = 0
        max_length = 0
        unique_hashset = set()

        while fast <len(s):
            while fast < len(s) and s[fast] not in unique_hashset:
                unique_hashset.add(s[fast])
                fast +=1

            max_length = max(max_length, len(unique_hashset))

            unique_hashset.remove(s[slow])
            slow +=1

        return max_length

if __name__ == '__main__':
    main()

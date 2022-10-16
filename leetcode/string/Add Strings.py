def main():
    so = Solution()
    print(so.addStrings(num1="9", num2="99"))


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2int(num):
            output = 0
            for d in num:
                output = output * 10 + (ord(d) - ord('0'))
            return output

        return str(str2int(num1) + str2int(num2))


if __name__ == '__main__':
    main()
# res = []
# carry = 0
# num1 = list(num1)
# num2 = list(num2)
# while len(num1) > 0 or len(num2) > 0 or carry > 0:
#     if len(num1) > 0:
#         n1 = ord(num1.pop()) - ord('0')
#     else:
#         n1 = 0
#     if len(num2) > 0:
#         n2 = ord(num2.pop()) - ord('0')
#     else:
#         n2 = 0
#
#     tmp = n1 + n2 + carry
#     res.append(tmp % 10)
#     carry = tmp // 10
# if carry: res.append(carry)
# return ''.join(str(i) for i in res)[::-1]

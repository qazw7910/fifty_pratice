def main():
    print(dailyTemperatures(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)
    stack = []
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i-cur
        stack.append(i)
    return ans


if __name__ == '__main__':
    main()

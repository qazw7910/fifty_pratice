def main():
    solution = Solution()
    print(solution.AsteroidCollision(asteroids=[5, 10, -5]))


class Solution:
    def AsteroidCollision(self, asteroids):
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()
        return stack


if __name__ == '__main__':
    main()

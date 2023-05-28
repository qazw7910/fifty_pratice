import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lookup = collections.defaultdict(list)

        for course, pre in prerequisites:
            lookup[course].append(pre)

        seen = set()

        def dfs(course):
            if course in seen:
                return False
            if lookup[course] == []:
                return True

            seen.add(course)

            for pre in lookup[course]:
                if not dfs(pre):
                    return False
            seen.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[0, 1], [0, 2], [1, 3], [2, 3]]
    so = Solution()
    print(so.canFinish(numCourses, prerequisites))

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        return

    def has_value(self, value):
        if self.data == value:
            return True
        else:
            return False



class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next


if __name__ == '__main__':
    solution = Solution()
    print(solution.middleNode(head=[1, 2, 3, 4, 5]))

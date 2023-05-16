from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def create_list_node(nums):
    head = ListNode(nums[0])
    cur_node = head
    i = 1
    while i < len(nums):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next
        i += 1
    return head

class Solution:
    # solution 1
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     dummy_node = ListNode(0)
    #     dummy_node.next = head
    #     length = 0
    #
    #     while head: # stop in next=None
    #         head = head.next
    #         length += 1
    #
    #     length -= n
    #     head = dummy_node
    #
    #     for i in range(length):
    #         head = head.next
    #
    #     head.next = head.next.next
    #
    #     return dummy_node.next
    # solution 2
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        fast = dummy_node
        slow = dummy_node

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy_node.next





if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]  # n = 2
    head = create_list_node(nums)
    so = Solution()
    print(so.removeNthFromEnd(head, n=2))


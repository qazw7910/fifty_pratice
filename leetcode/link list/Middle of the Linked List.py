class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# create the first node
head = ListNode(1)

# create the second node and link it to the first node
head.next = ListNode(2)

# create the third node and link it to the second node
head.next.next = ListNode(3)

head.next.next.next = ListNode(4)

head.next.next.next.next = ListNode(5)

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == '__main__':
    so = Solution()
    print(so.middleNode(head).next.next.val)
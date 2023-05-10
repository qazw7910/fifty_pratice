class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# create the first node
head = ListNode(1)
current_node = head
for i in range(2, 6):
    current_node.next = ListNode(i)
    current_node = current_node.next

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
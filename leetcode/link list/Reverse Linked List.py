from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)

head = ListNode(1)
current_node = head
for i in range(2, 6):
    current_node.next = ListNode(i)
    current_node = current_node.next


def get_node_value(node):
    if node is None:
        return []
    else:
        return [node.val] + get_node_value(node.next)

def main():

    print(f"before : {get_node_value(head)}")
    so = Solution()
    reverse_list = so.reverseList(head)
    print(f"after  : {get_node_value(reverse_list)}")


class Solution:
    # Solution iterative
    # def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     while head:
    #         next_node = head.next
    #         head.next = prev
    #         prev = head
    #         head = next_node
    #
    #     return prev
    # -----------------------------------------------------------------------
    # Solution Recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: # None or [1]
            return head

        reverse_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return reverse_head


if __name__ == '__main__':
    main()
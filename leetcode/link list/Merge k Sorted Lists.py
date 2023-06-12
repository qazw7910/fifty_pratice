from heapq import heapify, heappop, heappush
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_listnode(nums: List) -> ListNode:
    if not nums:
        return None

    head = ListNode(nums[0])
    cur_node = head

    for i in range(1, len(nums)):
        cur_node.next = ListNode(nums[i])
        cur_node = cur_node.next

    return head


def get_listnode_value(head: Optional[ListNode]):
    value = []
    cur = head

    while cur:
        value.append(cur.val)
        cur = cur.next

    return value


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for idx, linked_lsit in enumerate(lists):
            if linked_lsit:
                min_heap.append((linked_lsit.val, idx))

        heapify(min_heap)
        head = ListNode(None)
        dummy = head

        while min_heap:
            val, idx = heappop(min_heap)
            head.next = ListNode(val)
            head = head.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(min_heap, (lists[idx].val, idx))

        return dummy.next


if __name__ == '__main__':

    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    list_nodes = []

    for list in lists:
        list_node = create_listnode(list)
        list_nodes.append(list_node)

    so = Solution()
    print(get_listnode_value(so.mergeKLists(list_nodes)))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        # 首先對兩個鏈表進行遍歷，然后將數字轉化為字串加起來
        # 然后對整個字串進行逆序，在逆序的同時賦值給新創建的鏈表

        # 首先考慮為0的情況

        # 考慮鏈表不為0的情況
        l1_node = []
        l2_node = []
        # 在儲存進陣列里的時候可以直接逆序
        while l1:
            l1_node.insert(0, str(l1.val))
            l1 = l1.next

        while l2:
            l2_node.insert(0, str(l2.val))
            l2 = l2.next
        # 轉化為整數進行相加
        zhengshu = ''
        zhengshuer = ''
        for i in l1_node:
            zhengshu = zhengshu + i

        for j in l2_node:
            zhengshuer = zhengshuer + j

        zhengshu = int(zhengshu)
        zhengshuer = int(zhengshuer)

        summ = str(zhengshu + zhengshuer)
        # 將相加得到的整數再次變成字串，并分割，分別賦值給新的鏈表
        ls = []
        for i in summ:
            ls.append(i)
        node = ListNode(0)
        pointer = node
        # 這里還要進行倒序一次
        i = len(ls) - 1
        while i >= 0:
            node.next = ListNode(int(ls[i]))
            node = node.next
            i = i - 1

        return pointer.next

if __name__ == '__main__':
    so = Solution()
    print(so.addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
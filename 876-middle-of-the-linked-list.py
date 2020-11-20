        if not head:
            return None

        if not head.next:
            return head

#         count = 1
#         node = head
#         while node.next:
#             node = node.next
#             count += 1

#         middle = count // 2 if count^1 else count // 2 + 1
#         node = head
#         for i in range(middle):
#             node = node.next
#         return node

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

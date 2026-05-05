# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1 = list1
        node2 = list2

        head = None

        if not list1:
            return list2
        elif not list2:
            return list1

        if node1.val > node2.val:
            head = node2
            node2 = node2.next
        else:
            head = node1
            node1 = node1.next
        
        combList = head

        while node1 and node2:
            if node1.val > node2.val:
               combList.next = node2
               node2 = node2.next
            else:
                combList.next = node1
                node1 = node1.next
            combList = combList.next
        
        if node1:
            combList.next = node1
        
        if node2:
            combList.next = node2

        return head






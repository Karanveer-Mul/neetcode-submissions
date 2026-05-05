# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        num1 = 0
        num2 = 0

        output = ListNode(0)
        curNode = output

        i = 0
        while l1 and l2:
            value = curNode.val + l1.val + l2.val
            rem = value // 10

            curNode.val = value % 10
           
            l1 = l1.next
            l2 = l2.next

            if l1 or l2 or rem != 0:
                tmp = ListNode((rem if rem > 0 else 0))                
                curNode.next = tmp
                curNode = curNode.next

        while l1:
            value = curNode.val + l1.val
            rem = value // 10

            curNode.val = value % 10
           
            l1 = l1.next

            if l1 or rem != 0:
                tmp = ListNode((rem if rem > 0 else 0))                
                curNode.next = tmp
                curNode = curNode.next
        
        while l2:
            value = curNode.val + l2.val
            rem = value // 10

            curNode.val = value % 10
           
            l2 = l2.next

            if l2 or rem != 0:
                tmp = ListNode((rem if rem > 0 else 0))                
                curNode.next = tmp
                curNode = curNode.next

        return output